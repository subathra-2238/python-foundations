class MessageProcessor:

    def __init__(self):
        self.processed_ids = set()

    def process_message(self, message_id, message):

        if message_id in self.processed_ids:
            print(f"Duplicate ignored: {message}")
            return

        self.processed_ids.add(message_id)
        print(f"Processed: {message}")


processor = MessageProcessor()

processor.process_message(101, "Order 101")
processor.process_message(102, "Payment 102")
processor.process_message(101, "Order 101")
processor.process_message(103, "Order 103")
processor.process_message(102, "Payment 102")
