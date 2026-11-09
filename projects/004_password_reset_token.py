import secrets
import hashlib
import hmac


class PasswordResetSystem:

    def __init__(self):

        self.password = "OldPassword123"
        self.reset_token_hash = None

    def generate_reset_token(self):

        token = secrets.token_urlsafe(32)

        self.reset_token_hash = hashlib.sha256(
            token.encode()
        ).digest()

        return token

    def reset_password(self, token, new_password):

        if self.reset_token_hash is None:
            print("No active reset token!")
            return

        entered_hash = hashlib.sha256(
            token.encode()
        ).digest()

        if hmac.compare_digest(
            entered_hash,
            self.reset_token_hash
        ):

            self.password = new_password
            self.reset_token_hash = None

            print("Password reset successful!")

        else:
            print("Invalid reset token!")


system = PasswordResetSystem()

print("Old Password:", system.password)

# Generate reset token
token = system.generate_reset_token()

print("\nReset Token:", token)

# Reset password
print("\nResetting Password:")

system.reset_password(
    token,
    "NewPassword123"
)

print("\nUpdated Password:", system.password)

# Try reusing the same token
print("\nReusing Old Token:")

system.reset_password(
    token,
    "AnotherPassword123"
)
