import hashlib


class MessageHasher:

    def generate_hash(self, message):

        hash_object = hashlib.sha256(
            message.encode("utf-8")
        )

        return hash_object.hexdigest()

    def verify_message(self, message, original_hash):

        new_hash = self.generate_hash(message)

        if new_hash == original_hash:
            print("Message integrity verified!")
        else:
            print("Message has been modified!")


hasher = MessageHasher()

message = "Hello from AI Department"

original_hash = hasher.generate_hash(message)

print("Original Message:", message)
print("SHA-256 Hash:", original_hash)

print("\nChecking original message:")
hasher.verify_message(message, original_hash)

print("\nChecking modified message:")
hasher.verify_message(
    "Hello from Robotics Department",
    original_hash
)
