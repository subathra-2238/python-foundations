class DynamicLoadBalancer:

    def __init__(self, servers):
        self.servers = servers

    def add_server(self, name, load):
        self.servers[name] = load
        print(f"{name} added!")

    def update_load(self, name, load):
        if name in self.servers:
            self.servers[name] = load

    def get_server(self):

        if not self.servers:
            return None

        return min(
            self.servers,
            key=self.servers.get
        )

    def show_servers(self):
        for name, load in self.servers.items():
            print(f"{name}: {load}% load")


servers = {
    "Server 1": 70,
    "Server 2": 30,
    "Server 3": 50
}

balancer = DynamicLoadBalancer(servers)

print("Initial Server Loads:")
balancer.show_servers()

print("\nSelected Server:")
print(balancer.get_server())

balancer.update_load("Server 2", 90)

print("\nAfter Load Update:")
balancer.show_servers()

print("\nNew Selected Server:")
print(balancer.get_server())
