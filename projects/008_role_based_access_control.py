class AccessControl:

    def __init__(self):

        self.roles = {
            "admin": ["view", "add", "delete"],
            "editor": ["view", "add"],
            "viewer": ["view"]
        }

    def check_permission(self, username, role, action):

        if role not in self.roles:
            print("Invalid role!")
            return

        if action in self.roles[role]:

            print(f"{username} is allowed to {action}.")

        else:

            print(f"{username} is NOT allowed to {action}.")


system = AccessControl()

print("Admin Access:")
system.check_permission("Subathra", "admin", "delete")

print("\nEditor Access:")
system.check_permission("Sivasri", "editor", "add")

print("\nViewer Access:")
system.check_permission("Thilaga", "viewer", "delete")

print("\nInvalid Role:")
system.check_permission("User1", "guest", "view")
