import docker

from roheboam.engine.utils.convenience import run_shell_command


def stream_docker_logs(log_generator):
    while True:
        try:
            output = log_generator.__next__()
            if "stream" in output:
                output_str = output["stream"].strip("\r\n").strip("\n")
                print(output_str)
        except StopIteration:
            print("Docker image build complete.")
            break
        except ValueError:
            print(f"Error parsing output from docker image build: {output}")


def remove_image(image, force=True, no_prune=False):
    client = docker.from_env()
    client.images.remove(image=image, force=force, noprune=no_prune)


def build_image(image_tag, docker_file_path):
    # client = docker.from_env()
    # image, log_generator = client.images.build(path=docker_file_path, tag=image_tag)
    # stream_docker_logs(log_generator)

    # Have to use this workaround or the layers won't cache for some reason...
    run_shell_command(f"docker build {docker_file_path} -t {image_tag}")
