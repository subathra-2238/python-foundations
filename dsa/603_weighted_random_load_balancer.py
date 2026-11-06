import random


class WeightedRandomLoadBalancer:

    def __init__(self, servers):
        self.servers = list(servers.keys())
        self.weights = list(servers.values())

    def get_server(self):
        return random.choices(
            self.servers,
            weights=self.weights,
            k=1
        )[0]


servers = {
    "Server 1": 5,
    "Server 2": 3,
    "Server 3": 2
}

balancer = WeightedRandomLoadBalancer(servers)

for request in range(1, 11):
    server = balancer.get_server()
    print(f"Request {request} -> {server}")
