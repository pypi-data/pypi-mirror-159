import importlib.util
import shutil
import sys
import tempfile
from pathlib import Path
from textwrap import dedent

import conda_pack

from roheboam.engine.integrations.docker.utils import build_image
from roheboam.engine.logger import logger
from roheboam.engine.utils.convenience import run_shell_command

# def containerise_model(
#     model_path, model_format, model_image_name, build_env_image=None, conda_env="CURRENT", use_conda_pack=False, roheboam_dev_build=False
# ):
#     """Generates a Docker Image for the model
#     Args:
#         model_path (str): path to directory containing the model generated from MLFlow
#         model_format (str): Choose from 'MLFLOW', or 'SELDON'
#         build_env_image (str, optional): The image used for build the environment. Defaults to None. If it is None, it will use
#         the Python image for the current version of Python with some additional dependencies
#         conda_env (str, optional): The conda environment used. Defaults to None. If it is None & it detects a conda environment
#         it will use conda-pack as the default environment
#     """

#     model_path = Path(model_path)
#     logger.info("Creating Docker file")
#     docker_file = _create_docker_file(model_path, model_format, build_env_image, roheboam_dev_build)
#     logger.info("Creating image")
#     image = _create_image(docker_file, model_path, model_image_name, conda_env, roheboam_dev_build)
#     return image

# def _create_image(docker_file, model_path, model_image_name, conda_env, roheboam_dev_build):
#     with tempfile.TemporaryDirectory() as temp_dir:
#         if roheboam_dev_build:
#             logger.info("Copying roheboam source to build directory")
#             _copy_roheboam(temp_dir)
#         logger.info(f"Copying model from {model_path} to build directory")
#         _copy_model(model_path, temp_dir)
#         logger.info(f"Copying conda env to build directory")
#         _copy_conda_env(conda_env, temp_dir)
#         logger.info(f"Writing Docker file")
#         _write_docker_file(docker_file, temp_dir)
#         logger.info(f"Building image")
#         image = build_image(model_image_name, temp_dir)
#         return image


def containerise_model(
    model_path, model_format, model_image_name, build_env_image=None, conda_env="CURRENT", use_conda_pack=False, roheboam_dev_build=False
):
    with tempfile.TemporaryDirectory() as temp_dir:
        if roheboam_dev_build:
            logger.info("Copying roheboam source to build directory")
            _copy_roheboam(temp_dir)

        if use_conda_pack:
            logger.info(f"Copying conda env to build directory")
            _copy_conda_env(conda_env, temp_dir)
        else:
            _export_conda_env(temp_dir)

        logger.info(f"Copying model from {model_path} to build directory")
        _copy_model(model_path, temp_dir)

        logger.info(f"Creating Docker file")
        docker_file = _create_docker_file(model_path, model_format, build_env_image, use_conda_pack, roheboam_dev_build)

        logger.info(f"Writing Docker file")
        _write_docker_file(docker_file, temp_dir)

        logger.info(f"Building image at {temp_dir}")
        image = build_image(model_image_name, temp_dir)

        return image


def _copy_model(model_path, save_path):
    shutil.copytree(model_path, f"{save_path}/{model_path.name}")


def _copy_roheboam(save_path):
    roheboam_project_path = Path(importlib.util.find_spec("roheboam").origin).parent.parent
    shutil.copytree(roheboam_project_path / "roheboam", f"{save_path}/roheboam/roheboam")
    shutil.copytree(roheboam_project_path / "requirements", f"{save_path}/roheboam/requirements")
    shutil.copy2(roheboam_project_path / "setup.py", f"{save_path}/roheboam/setup.py")


def _copy_conda_env(conda_env, save_path):
    if conda_env is None:
        return

    if conda_env == "CURRENT":
        conda_pack.pack(output=f"{save_path}/conda_env.tar.gz", n_threads=-1, ignore_editable_packages=True)
        return

    conda_pack.pack(name=conda_env, output=f"{save_path}/conda_env.tar.gz", n_threads=-1, ignore_editable_packages=True)


def _export_conda_env(save_path):
    run_shell_command(f"conda env export > {save_path}/env.yml")


def _create_docker_file(model_path, model_format, build_env_image, use_conda_pack=False, roheboam_dev_build=False):
    if build_env_image:
        build_env_image = build_env_image
    else:
        major_version, minor_version, *_ = sys.version_info
        build_env_image = f"python:{major_version}.{minor_version}"

    docker_template = dedent(
        f"""
        FROM {build_env_image}
        RUN apt-get update && DEBIAN_FRONTEND="noninteractive" apt-get install \
            'ffmpeg'\
            'libsm6' \
            'libxext6' \
            'libvips-dev' -y
        ENV SSL_CERT_DIR=/etc/ssl/certs
        """
    )

    if use_conda_pack:
        docker_template += dedent(
            f"""
            RUN mkdir -p /conda/conda_env
            COPY ./conda_env.tar.gz /conda/conda_env.tar.gz
            RUN tar -xzf /conda/conda_env.tar.gz -C /conda/conda_env
            ENV PATH="/conda/conda_env/bin:$PATH"
            """
        )
    else:
        docker_template += dedent(
            f"""
            COPY env.yml /home/build/conda/env.yml
            RUN conda env create -f /home/build/conda/env.yml -n roheboam
            ENV PATH="/opt/conda/envs/roheboam/bin:$PATH"
            """
        )

    if roheboam_dev_build:
        docker_template += dedent(
            f"""
            COPY ./roheboam /home/build/roheboam
            WORKDIR /home/build/roheboam
            RUN python setup.py install
            """
        )

    docker_template += dedent(
        f"""
            RUN mkdir -p /home/model
            WORKDIR /home/model
            COPY {model_path.name} /home/model
            RUN mkdir -p /home/.cache
            ENV TORCH_HOME=/home/.cache
            RUN chmod -R 777 /home
        """
    )

    if model_format == "MLFLOW":
        docker_template += dedent(
            f"""
           CMD exec roheboam serve --model_path /home/model --model_format mlflow
        """
        )

    if model_format == "SELDON":
        docker_template += dedent(
            f"""
            # Port for GRPC
            EXPOSE 5000
            # Port for REST
            EXPOSE 9000

            # Define environment variables
            ENV MODEL_NAME roheboam.engine.vision.SeldonImageModel
            ENV SERVICE_TYPE MODEL
            ENV SELDON_MODEL_PATH /home/model
            ENV FLASK_SINGLE_THREADED 1
            CMD exec roheboam serve --model_path /home/model --model_format seldon --debug
        """
        )
    return docker_template


def _write_docker_file(docker_file, save_path):
    with (Path(save_path) / "Dockerfile").open("w") as f:
        f.write(docker_file)
