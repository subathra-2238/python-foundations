class FailoverLoadBalancer:

    def __init__(self, servers):
        self.servers = servers

    def get_server(self):

        for server in self.servers:

            if server["active"]:
                return server["name"]

        return None

    def deactivate_server(self, name):

        for server in self.servers:
            if server["name"] == name:
                server["active"] = False
                print(f"{name} deactivated!")


servers = [
    {"name": "Primary Server", "active": True},
    {"name": "Backup Server 1", "active": True},
    {"name": "Backup Server 2", "active": True}
]

balancer = FailoverLoadBalancer(servers)

print("Selected:", balancer.get_server())

balancer.deactivate_server("Primary Server")

print("After failure:", balancer.get_server())

balancer.deactivate_server("Backup Server 1")

print("After second failure:", balancer.get_server())
