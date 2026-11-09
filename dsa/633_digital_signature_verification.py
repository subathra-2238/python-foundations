from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import hashes


class DigitalSignature:

    def __init__(self):

        self.private_key = rsa.generate_private_key(
            public_exponent=65537,
            key_size=2048
        )

        self.public_key = self.private_key.public_key()

    def sign_message(self, message):

        signature = self.private_key.sign(
            message.encode(),
            padding.PSS(
                mgf=padding.MGF1(hashes.SHA256()),
                salt_length=padding.PSS.MAX_LENGTH
            ),
            hashes.SHA256()
        )

        print("Digital signature generated!")
        return signature

    def verify_signature(self, message, signature):

        try:
            self.public_key.verify(
                signature,
                message.encode(),
                padding.PSS(
                    mgf=padding.MGF1(hashes.SHA256()),
                    salt_length=padding.PSS.MAX_LENGTH
                ),
                hashes.SHA256()
            )

            print("Signature verified successfully!")

        except Exception:
            print("Signature verification failed!")


system = DigitalSignature()

message = "Approve payment of Rs.1000"

signature = system.sign_message(message)

print("\nVerifying original message:")
system.verify_signature(message, signature)

print("\nVerifying modified message:")
system.verify_signature(
    "Approve payment of Rs.5000",
    signature
)
