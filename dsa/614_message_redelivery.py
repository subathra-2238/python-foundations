from collections import deque


class MessageBroker:

    def __init__(self):
        self.queue = deque()
        self.processed = []

    def send_message(self, message):
        self.queue.append({
            "message": message,
            "attempts": 0
        })
        print(f"Sent: {message}")

    def process_next(self):

        if not self.queue:
            print("No messages available")
            return

        item = self.queue.popleft()
        message = item["message"]

        item["attempts"] += 1

        # Simulate failure on the first attempt
        if message == "Payment 102" and item["attempts"] == 1:
            print(f"Processing failed: {message}")
            print(f"Redelivering: {message}")
            self.queue.append(item)

        else:
            print(f"Successfully processed: {message}")
            self.processed.append(message)

    def show_status(self):
        print("Pending:", [
            item["message"] for item in self.queue
        ])
        print("Processed:", self.processed)


broker = MessageBroker()

broker.send_message("Order 101")
broker.send_message("Payment 102")

broker.process_next()
broker.process_next()
broker.process_next()

broker.show_status()
