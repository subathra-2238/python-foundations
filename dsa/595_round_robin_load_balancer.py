class LoadBalancer:

    def __init__(self, servers):
        self.servers = servers
        self.current_index = 0

    def get_server(self):

        server = self.servers[self.current_index]

        self.current_index = (
            self.current_index + 1
        ) % len(self.servers)

        return server


servers = ["Server 1", "Server 2", "Server 3"]

balancer = LoadBalancer(servers)

for request in range(1, 8):
    server = balancer.get_server()
    print(f"Request {request} -> {server}")
