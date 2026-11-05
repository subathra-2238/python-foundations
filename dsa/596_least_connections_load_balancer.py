class LoadBalancer:

    def __init__(self, servers):
        self.connections = {
            server: 0 for server in servers
        }

    def get_server(self):

        server = min(
            self.connections,
            key=self.connections.get
        )

        self.connections[server] += 1

        return server

    def release_connection(self, server):
        if self.connections[server] > 0:
            self.connections[server] -= 1

    def show_connections(self):
        for server, count in self.connections.items():
            print(f"{server}: {count} connections")


servers = ["Server 1", "Server 2", "Server 3"]

balancer = LoadBalancer(servers)

for request in range(1, 7):
    server = balancer.get_server()
    print(f"Request {request} -> {server}")

print("\nConnection Status:")
balancer.show_connections()
