from collections import deque


class MessageQueue:

    def __init__(self):
        self.queue = deque()

    def add_message(self, message):
        self.queue.append(message)
        print(f"Received: {message}")

    def process_messages(self):

        print("\nProcessing messages:")

        while self.queue:
            message = self.queue.popleft()
            print(f"Processed: {message}")


manager = MessageQueue()

manager.add_message("Message 101")
manager.add_message("Message 102")
manager.add_message("Message 103")
manager.add_message("Message 104")

manager.process_messages()
