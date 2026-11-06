class WeightedHealthLoadBalancer:

    def __init__(self, servers):
        self.servers = servers

    def get_server(self):

        available = [
            server for server in self.servers
            if server["healthy"]
        ]

        if not available:
            return None

        selected = max(
            available,
            key=lambda server: server["weight"]
        )

        return selected["name"]

    def update_health(self, name, status):

        for server in self.servers:
            if server["name"] == name:
                server["healthy"] = status

    def show_servers(self):

        for server in self.servers:
            print(
                f'{server["name"]}: '
                f'Weight={server["weight"]}, '
                f'Healthy={server["healthy"]}'
            )


servers = [
    {"name": "Server 1", "weight": 5, "healthy": True},
    {"name": "Server 2", "weight": 3, "healthy": True},
    {"name": "Server 3", "weight": 8, "healthy": False}
]

balancer = WeightedHealthLoadBalancer(servers)

print("Server Status:")
balancer.show_servers()

print("\nSelected Server:")
print(balancer.get_server())

balancer.update_health("Server 3", True)

print("\nAfter Health Update:")
print(balancer.get_server())
