class MessageBatcher:

    def __init__(self, batch_size):
        self.batch_size = batch_size
        self.messages = []

    def add_message(self, message):
        self.messages.append(message)
        print(f"Added: {message}")

        if len(self.messages) >= self.batch_size:
            self.process_batch()

    def process_batch(self):

        if not self.messages:
            print("No messages to process")
            return

        print("\nProcessing Batch:")

        for message in self.messages:
            print(f"Processed: {message}")

        self.messages.clear()
        print("Batch completed!\n")


batcher = MessageBatcher(batch_size=3)

batcher.add_message("Order 101")
batcher.add_message("Order 102")
batcher.add_message("Order 103")

batcher.add_message("Order 104")
batcher.add_message("Order 105")

print("Processing remaining messages:")
batcher.process_batch()
