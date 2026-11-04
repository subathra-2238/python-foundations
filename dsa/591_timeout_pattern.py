import time
from concurrent.futures import ThreadPoolExecutor, TimeoutError


def slow_operation():
    time.sleep(5)
    return "Operation completed!"


with ThreadPoolExecutor() as executor:

    future = executor.submit(slow_operation)

    try:
        result = future.result(timeout=2)
        print(result)

    except TimeoutError:
        print("Operation timed out!")
