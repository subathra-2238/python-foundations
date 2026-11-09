class AttributeAccessControl:

    def check_access(self, user, resource):

        if (
            user["department"] == resource["department"]
            and user["role"] == "admin"
            and resource["status"] == "active"
        ):

            return "Access Granted!"

        return "Access Denied!"


system = AttributeAccessControl()

user = {
    "name": "Subathra",
    "role": "admin",
    "department": "AI&ML"
}

resource = {
    "name": "AI Project File",
    "department": "AI&ML",
    "status": "active"
}

print("User:", user["name"])
print("Resource:", resource["name"])

print("\nChecking Access:")
print(system.check_access(user, resource))

# Try accessing another department
resource["department"] = "Robotics"

print("\nChecking Different Department:")
print(system.check_access(user, resource))
