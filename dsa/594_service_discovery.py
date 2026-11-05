class ServiceRegistry:

    def __init__(self):
        self.services = {}

    def register_service(self, name, address):
        self.services[name] = address
        print(f"{name} registered successfully!")

    def discover_service(self, name):

        if name in self.services:
            print(f"{name} found at {self.services[name]}")
        else:
            print(f"{name} not found!")


registry = ServiceRegistry()

registry.register_service("User Service", "192.168.1.10")
registry.register_service("Payment Service", "192.168.1.20")
registry.register_service("Order Service", "192.168.1.30")

print("\nService Discovery:")

registry.discover_service("Payment Service")
registry.discover_service("Notification Service")
