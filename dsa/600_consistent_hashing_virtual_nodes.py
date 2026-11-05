import hashlib


class ConsistentHashing:

    def __init__(self, servers, virtual_nodes=3):
        self.ring = {}
        self.virtual_nodes = virtual_nodes

        for server in servers:
            self.add_server(server)

    def hash_value(self, key):
        return int(
            hashlib.md5(key.encode()).hexdigest(),
            16
        )

    def add_server(self, server):

        for i in range(self.virtual_nodes):
            virtual_node = f"{server}-{i}"
            position = self.hash_value(virtual_node)
            self.ring[position] = server

    def get_server(self, key):

        if not self.ring:
            return None

        key_position = self.hash_value(key)
        positions = sorted(self.ring)

        for position in positions:
            if key_position <= position:
                return self.ring[position]

        return self.ring[positions[0]]


servers = ["Server 1", "Server 2", "Server 3"]

hashing = ConsistentHashing(servers, virtual_nodes=3)

keys = ["User A", "User B", "User C", "User D"]

for key in keys:
    print(f"{key} -> {hashing.get_server(key)}")

print("\nTotal virtual nodes:", len(hashing.ring))
