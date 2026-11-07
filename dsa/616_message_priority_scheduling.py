import heapq


class MessageScheduler:

    def __init__(self):
        self.queue = []

    def add_message(self, message, priority):
        heapq.heappush(
            self.queue,
            (priority, len(self.queue), message)
        )
        print(f"Added: {message} (Priority: {priority})")

    def process_message(self):

        if not self.queue:
            print("No messages available")
            return

        priority, order, message = heapq.heappop(self.queue)

        print(f"Processing: {message} (Priority: {priority})")


scheduler = MessageScheduler()

scheduler.add_message("Normal Email", 3)
scheduler.add_message("Emergency Alert", 1)
scheduler.add_message("Important Notification", 2)

print("\nProcessing messages:")

scheduler.process_message()
scheduler.process_message()
scheduler.process_message()
