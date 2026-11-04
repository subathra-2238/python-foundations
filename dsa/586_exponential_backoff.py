import time


def retry_request(max_retries):

    delay = 1

    for attempt in range(1, max_retries + 1):

        print(f"Attempt {attempt}")

        success = attempt == 4

        if success:
            print("Request successful!")
            return True

        print(f"Failed! Retrying in {delay} seconds...")

        time.sleep(delay)

        delay *= 2

    print("All retries failed.")
    return False


retry_request(5)
