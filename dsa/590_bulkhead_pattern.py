from concurrent.futures import ThreadPoolExecutor
import time


class Bulkhead:

    def __init__(self, max_workers):
        self.executor = ThreadPoolExecutor(
            max_workers=max_workers
        )

    def execute_task(self, task_name):

        def task():
            print(f"{task_name} started")
            time.sleep(1)
            print(f"{task_name} completed")

        return self.executor.submit(task)


bulkhead = Bulkhead(2)

tasks = []

for i in range(5):
    tasks.append(
        bulkhead.execute_task(f"Task {i + 1}")
    )

for task in tasks:
    task.result()

bulkhead.executor.shutdown()
