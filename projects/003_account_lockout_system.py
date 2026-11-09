import hashlib
import secrets
import hmac


class AccountLockout:

    def __init__(self, max_attempts=3):

        self.username = "subathra"
        self.max_attempts = max_attempts
        self.failed_attempts = 0
        self.is_locked = False

        self.salt = secrets.token_bytes(16)

        self.password_hash = hashlib.pbkdf2_hmac(
            "sha256",
            b"MyPassword123",
            self.salt,
            100_000
        )

    def login(self, username, password):

        if self.is_locked:
            print("Account is locked!")
            return

        if username != self.username:
            print("Invalid username!")
            return

        entered_hash = hashlib.pbkdf2_hmac(
            "sha256",
            password.encode("utf-8"),
            self.salt,
            100_000
        )

        if hmac.compare_digest(
            entered_hash,
            self.password_hash
        ):

            self.failed_attempts = 0
            print("Login successful!")

        else:

            self.failed_attempts += 1

            remaining = (
                self.max_attempts - self.failed_attempts
            )

            print("Incorrect password!")

            if remaining == 0:
                self.is_locked = True
                print("Account locked!")
            else:
                print("Attempts remaining:", remaining)


system = AccountLockout()

print("Login Attempt 1:")
system.login("subathra", "wrong123")

print("\nLogin Attempt 2:")
system.login("subathra", "wrong456")

print("\nLogin Attempt 3:")
system.login("subathra", "wrong789")

print("\nLogin Attempt 4:")
system.login("subathra", "MyPassword123")
