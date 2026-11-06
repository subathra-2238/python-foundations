import random


class RandomLoadBalancer:

    def __init__(self, servers):
        self.servers = servers

    def get_server(self):
        return random.choice(self.servers)


servers = ["Server 1", "Server 2", "Server 3"]

balancer = RandomLoadBalancer(servers)

for request in range(1, 8):
    server = balancer.get_server()
    print(f"Request {request} -> {server}")
