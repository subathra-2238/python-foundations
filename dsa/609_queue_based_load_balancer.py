from collections import deque


class QueueLoadBalancer:

    def __init__(self, servers):
        self.servers = deque(servers)

    def get_server(self):

        if not self.servers:
            return None

        server = self.servers.popleft()
        self.servers.append(server)

        return server


servers = ["Server 1", "Server 2", "Server 3"]

balancer = QueueLoadBalancer(servers)

for request in range(1, 8):
    server = balancer.get_server()
    print(f"Request {request} -> {server}")
