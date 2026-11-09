class PermissionManager:

    def __init__(self):

        self.roles = {
            "viewer": {
                "permissions": ["read"],
                "parent": None
            },

            "editor": {
                "permissions": ["write"],
                "parent": "viewer"
            },

            "admin": {
                "permissions": ["delete"],
                "parent": "editor"
            }
        }

    def get_permissions(self, role):

        if role not in self.roles:
            return set()

        permissions = set(
            self.roles[role]["permissions"]
        )

        parent = self.roles[role]["parent"]

        if parent:
            permissions.update(
                self.get_permissions(parent)
            )

        return permissions

    def check_access(self, role, action):

        permissions = self.get_permissions(role)

        if action in permissions:
            print(f"{role} can {action}.")

        else:
            print(f"{role} cannot {action}.")


manager = PermissionManager()

print("Admin Permissions:")
print(manager.get_permissions("admin"))

print("\nEditor Permissions:")
print(manager.get_permissions("editor"))

print("\nChecking Access:")

manager.check_access("admin", "delete")
manager.check_access("editor", "read")
manager.check_access("viewer", "write")
