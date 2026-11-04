import time


def api_request(max_retries):

    for attempt in range(1, max_retries + 1):

        print(f"Attempt {attempt}")

        success = attempt == 3

        if success:
            print("Request successful!")
            return True

        print("Request failed. Retrying...")

        time.sleep(1)

    print("Maximum retries reached.")
    return False


api_request(5)
