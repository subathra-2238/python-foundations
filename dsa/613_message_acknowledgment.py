from collections import deque


class MessageBroker:

    def __init__(self):
        self.queue = deque()
        self.acknowledged = []

    def send_message(self, message):
        self.queue.append(message)
        print(f"Sent: {message}")

    def receive_message(self):

        if not self.queue:
            print("No messages available")
            return

        message = self.queue.popleft()

        print(f"Received: {message}")

        self.acknowledge(message)

    def acknowledge(self, message):
        self.acknowledged.append(message)
        print(f"ACK received for: {message}")

    def show_status(self):
        print("Pending messages:", list(self.queue))
        print("Acknowledged messages:", self.acknowledged)


broker = MessageBroker()

broker.send_message("Order 101")
broker.send_message("Payment 102")
broker.send_message("Order 103")

broker.receive_message()
broker.receive_message()

broker.show_status()
