import secrets
import hashlib
import hmac


class EmailVerification:

    def __init__(self, email):

        self.email = email
        self.is_verified = False
        self.token_hash = None

    def generate_token(self):

        token = secrets.token_urlsafe(32)

        self.token_hash = hashlib.sha256(
            token.encode("utf-8")
        ).digest()

        return token

    def verify_email(self, entered_token):

        if self.token_hash is None:
            print("No active verification token!")
            return

        entered_hash = hashlib.sha256(
            entered_token.encode("utf-8")
        ).digest()

        if hmac.compare_digest(
            entered_hash,
            self.token_hash
        ):

            self.is_verified = True
            self.token_hash = None

            print("Email verified successfully!")

        else:
            print("Invalid verification token!")


user = EmailVerification("subathra@example.com")

print("Email:", user.email)
print("Verified:", user.is_verified)

token = user.generate_token()

print("\nVerification Token:", token)

print("\nVerifying Email:")

user.verify_email(token)

print("\nAccount Status:")
print("Verified:", user.is_verified)

print("\nTrying to Reuse Token:")
user.verify_email(token)
