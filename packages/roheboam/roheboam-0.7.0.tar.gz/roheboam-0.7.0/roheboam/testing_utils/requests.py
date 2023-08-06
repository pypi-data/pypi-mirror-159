import time

import requests


def post_request_on_url_with_retry_until_success(url, data, attempts=5, per_try_timeout=5, completion_handler=lambda: None):
    try:
        for attempt in range(attempts):
            try:
                response = requests.post(
                    url,
                    data=data,
                    headers={"Content-Type": "application/json"},
                )
                assert response.status_code == 200
                print(f"Success on attempt: {attempt + 1}")
                break
            except Exception as e:
                print(f"Failure on attempt: {attempt + 1}")
                print(e)
                time.sleep(per_try_timeout)
    finally:
        completion_handler()


def stop_container_completion_handler(container, silent=True):
    try:
        if not silent:
            print(container.logs().decode())
        container.stop()
    except Exception as e:
        print(e)
