class WeightedLoadBalancer:

    def __init__(self, servers):
        self.servers = []

        for server, weight in servers.items():
            self.servers.extend([server] * weight)

        self.current_index = 0

    def get_server(self):

        server = self.servers[self.current_index]

        self.current_index = (
            self.current_index + 1
        ) % len(self.servers)

        return server


servers = {
    "Server 1": 3,
    "Server 2": 2,
    "Server 3": 1
}

balancer = WeightedLoadBalancer(servers)

for request in range(1, 13):
    print(
        f"Request {request} -> {balancer.get_server()}"
    )
