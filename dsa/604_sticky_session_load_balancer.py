class StickySessionLoadBalancer:

    def __init__(self, servers):
        self.servers = servers
        self.sessions = {}
        self.current_index = 0

    def get_server(self, session_id):

        if session_id in self.sessions:
            return self.sessions[session_id]

        server = self.servers[self.current_index]

        self.sessions[session_id] = server

        self.current_index = (
            self.current_index + 1
        ) % len(self.servers)

        return server


servers = ["Server 1", "Server 2", "Server 3"]

balancer = StickySessionLoadBalancer(servers)

sessions = [
    "User A",
    "User B",
    "User C",
    "User A",
    "User B",
    "User D"
]

for session in sessions:
    server = balancer.get_server(session)
    print(f"{session} -> {server}")
