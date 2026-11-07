from collections import deque


class RequestQueue:

    def __init__(self):
        self.queue = deque()

    def add_request(self, request):
        self.queue.append(request)
        print(f"{request} added to queue")

    def process_request(self):

        if not self.queue:
            print("No requests available")
            return

        request = self.queue.popleft()
        print(f"Processing: {request}")

    def show_queue(self):
        print("Pending Requests:", list(self.queue))


manager = RequestQueue()

manager.add_request("Request 101")
manager.add_request("Request 102")
manager.add_request("Request 103")

manager.show_queue()

manager.process_request()
manager.process_request()

manager.show_queue()
