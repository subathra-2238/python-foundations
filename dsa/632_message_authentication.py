import hmac
import hashlib


class MessageAuthenticator:

    def __init__(self, secret_key):
        self.secret_key = secret_key.encode()

    def generate_signature(self, message):

        signature = hmac.new(
            self.secret_key,
            message.encode(),
            hashlib.sha256
        ).hexdigest()

        return signature

    def verify_message(self, message, received_signature):

        expected_signature = self.generate_signature(message)

        if hmac.compare_digest(
            expected_signature,
            received_signature
        ):
            print("Message authenticated successfully!")
        else:
            print("Authentication failed! Message may be modified.")


authenticator = MessageAuthenticator("my_secret_key")

message = "Transfer Rs.1000"

signature = authenticator.generate_signature(message)

print("Original Message:", message)
print("Generated Signature:", signature)

print("\nVerifying original message:")
authenticator.verify_message(message, signature)

print("\nVerifying modified message:")
authenticator.verify_message("Transfer Rs.5000", signature)
