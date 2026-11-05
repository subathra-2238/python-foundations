import time


class HealthMonitor:

    def __init__(self):
        self.services = {
            "Database": True,
            "API": True,
            "Authentication": False
        }

    def check_health(self):

        for service, status in self.services.items():

            if status:
                print(f"{service}: HEALTHY")
            else:
                print(f"{service}: UNHEALTHY")

    def update_status(self, service, status):

        self.services[service] = status
        print(f"{service} status updated!")


monitor = HealthMonitor()

print("Initial Health Check:")
monitor.check_health()

print("\nUpdating Authentication Service:")
monitor.update_status("Authentication", True)

print("\nUpdated Health Check:")
monitor.check_health()
