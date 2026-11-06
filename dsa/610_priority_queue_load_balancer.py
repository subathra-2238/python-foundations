import heapq


class PriorityQueueLoadBalancer:

    def __init__(self, servers):
        self.servers = []
        self.counter = 0

        for name, priority in servers:
            heapq.heappush(
                self.servers,
                (priority, self.counter, name)
            )
            self.counter += 1

    def get_server(self):

        if not self.servers:
            return None

        priority, count, server = heapq.heappop(
            self.servers
        )

        return server


servers = [
    ("Server 1", 3),
    ("Server 2", 1),
    ("Server 3", 2)
]

balancer = PriorityQueueLoadBalancer(servers)

for request in range(1, 4):
    print(
        f"Request {request} -> {balancer.get_server()}"
    )
