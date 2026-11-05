import hashlib


class IPHashLoadBalancer:

    def __init__(self, servers):
        self.servers = servers

    def get_server(self, ip_address):

        hash_value = hashlib.md5(
            ip_address.encode()
        ).hexdigest()

        index = int(hash_value, 16) % len(self.servers)

        return self.servers[index]


servers = ["Server 1", "Server 2", "Server 3"]

balancer = IPHashLoadBalancer(servers)

ip_addresses = [
    "192.168.1.10",
    "192.168.1.20",
    "192.168.1.30",
    "192.168.1.10"
]

for ip in ip_addresses:
    server = balancer.get_server(ip)
    print(f"{ip} -> {server}")
