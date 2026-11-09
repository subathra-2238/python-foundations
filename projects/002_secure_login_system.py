import hashlib
import secrets
import hmac


class SecureLogin:

    def __init__(self):
        self.users = {}

    def register(self, username, password):

        salt = secrets.token_bytes(16)

        password_hash = hashlib.pbkdf2_hmac(
            "sha256",
            password.encode("utf-8"),
            salt,
            100_000
        )

        self.users[username] = (salt, password_hash)

        print("User registered successfully!")

    def login(self, username, password):

        if username not in self.users:
            print("User not found!")
            return

        salt, stored_hash = self.users[username]

        entered_hash = hashlib.pbkdf2_hmac(
            "sha256",
            password.encode("utf-8"),
            salt,
            100_000
        )

        if hmac.compare_digest(entered_hash, stored_hash):
            print("Login successful!")
        else:
            print("Incorrect password!")


system = SecureLogin()

# Register user
system.register("subathra", "MyPassword123")

# Correct login
print("\nCorrect Login:")
system.login("subathra", "MyPassword123")

# Incorrect login
print("\nIncorrect Login:")
system.login("subathra", "WrongPassword")
