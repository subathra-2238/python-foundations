class MessageLoadBalancer:

    def __init__(self, workers):
        self.workers = workers
        self.current = 0

    def distribute_message(self, message):

        worker = self.workers[self.current]

        print(f"{message} -> {worker}")

        self.current = (self.current + 1) % len(self.workers)


workers = ["Worker A", "Worker B", "Worker C"]

balancer = MessageLoadBalancer(workers)

messages = [
    "Message 101",
    "Message 102",
    "Message 103",
    "Message 104",
    "Message 105",
    "Message 106"
]

for message in messages:
    balancer.distribute_message(message)
