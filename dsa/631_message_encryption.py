from cryptography.fernet import Fernet


class MessageEncryption:

    def __init__(self):
        self.key = Fernet.generate_key()
        self.cipher = Fernet(self.key)

    def encrypt_message(self, message):

        encrypted = self.cipher.encrypt(
            message.encode()
        )

        print("Encrypted Message:")
        print(encrypted.decode())

        return encrypted

    def decrypt_message(self, encrypted):

        decrypted = self.cipher.decrypt(encrypted)

        print("\nDecrypted Message:")
        print(decrypted.decode())


system = MessageEncryption()

message = "Hello from AI Department"

encrypted_message = system.encrypt_message(message)

system.decrypt_message(encrypted_message)
