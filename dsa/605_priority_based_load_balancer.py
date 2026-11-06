class PriorityLoadBalancer:

    def __init__(self, servers):
        self.servers = servers

    def get_server(self):

        available_servers = [
            server for server in self.servers
            if server["active"]
        ]

        if not available_servers:
            return None

        selected = min(
            available_servers,
            key=lambda server: server["priority"]
        )

        return selected["name"]


servers = [
    {"name": "Server 1", "priority": 2, "active": True},
    {"name": "Server 2", "priority": 1, "active": True},
    {"name": "Server 3", "priority": 3, "active": True}
]

balancer = PriorityLoadBalancer(servers)

for request in range(1, 5):
    print(
        f"Request {request} -> {balancer.get_server()}"
    )
