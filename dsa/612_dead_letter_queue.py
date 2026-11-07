from collections import deque


class DeadLetterQueue:

    def __init__(self, max_retries):
        self.pending = deque()
        self.dead_letters = deque()
        self.max_retries = max_retries

    def add_message(self, message):
        self.pending.append({
            "message": message,
            "attempts": 0
        })
        print(f"Added: {message}")

    def process_messages(self):

        while self.pending:
            item = self.pending.popleft()
            message = item["message"]

            # Simulate a failure for Payment 102
            if message == "Payment 102":
                item["attempts"] += 1

                print(
                    f"Failed: {message} "
                    f"(attempt {item['attempts']})"
                )

                if item["attempts"] < self.max_retries:
                    self.pending.append(item)
                else:
                    self.dead_letters.append(message)
                    print(f"Moved to dead-letter queue: {message}")

            else:
                print(f"Processed: {message}")

    def show_queues(self):
        print("Pending:", list(self.pending))
        print("Dead letters:", list(self.dead_letters))


manager = DeadLetterQueue(max_retries=2)

manager.add_message("Order 101")
manager.add_message("Payment 102")
manager.add_message("Order 103")

manager.process_messages()

manager.show_queues()
