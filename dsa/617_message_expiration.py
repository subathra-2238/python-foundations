import time


class MessageQueue:

    def __init__(self):
        self.queue = []

    def add_message(self, message, ttl):
        expiry_time = time.time() + ttl

        self.queue.append({
            "message": message,
            "expiry": expiry_time
        })

        print(f"Added: {message} (TTL: {ttl} seconds)")

    def process_messages(self):

        current_time = time.time()

        for item in self.queue:

            if current_time >= item["expiry"]:
                print(f"Expired: {item['message']}")
            else:
                print(f"Processing: {item['message']}")

        self.queue.clear()


manager = MessageQueue()

manager.add_message("Order 101", 10)
manager.add_message("OTP 202", 0)

manager.process_messages()
