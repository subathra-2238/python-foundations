class HealthBasedLoadBalancer:

    def __init__(self, servers):
        self.servers = {
            server: True for server in servers
        }

    def update_health(self, server, status):
        self.servers[server] = status

    def get_server(self):

        for server, healthy in self.servers.items():

            if healthy:
                return server

        return None

    def show_servers(self):
        for server, healthy in self.servers.items():
            status = "Healthy" if healthy else "Unhealthy"
            print(f"{server}: {status}")


servers = ["Server 1", "Server 2", "Server 3"]

balancer = HealthBasedLoadBalancer(servers)

balancer.update_health("Server 1", False)
balancer.update_health("Server 2", True)
balancer.update_health("Server 3", False)

print("Server Health:")
balancer.show_servers()

print("\nSelected Server:")
print(balancer.get_server())
