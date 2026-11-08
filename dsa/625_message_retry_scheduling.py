import heapq


class RetryScheduler:

    def __init__(self):
        self.retry_queue = []

    def schedule_retry(self, message, delay):

        heapq.heappush(
            self.retry_queue,
            (delay, message)
        )

        print(f"Retry scheduled: {message} after {delay} seconds")

    def process_retries(self):

        print("\nRetry Schedule:")

        while self.retry_queue:
            delay, message = heapq.heappop(self.retry_queue)

            print(f"Retrying: {message} after {delay} seconds")


scheduler = RetryScheduler()

scheduler.schedule_retry("Payment 101", 5)
scheduler.schedule_retry("Order 102", 2)
scheduler.schedule_retry("Notification 103", 8)

scheduler.process_retries()
