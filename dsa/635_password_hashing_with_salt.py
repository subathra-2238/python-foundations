import hashlib
import secrets
import hmac


class PasswordHasher:

    def hash_password(self, password):

        salt = secrets.token_bytes(16)

        stored_hash = hashlib.pbkdf2_hmac(
            "sha256",
            password.encode("utf-8"),
            salt,
            100_000
        )

        return salt, stored_hash

    def verify_password(self, password, salt, stored_hash):

        new_hash = hashlib.pbkdf2_hmac(
            "sha256",
            password.encode("utf-8"),
            salt,
            100_000
        )

        return hmac.compare_digest(new_hash, stored_hash)


hasher = PasswordHasher()

password = "MyStrongPassword123"

salt, stored_hash = hasher.hash_password(password)

print("Salt:", salt.hex())
print("Password Hash:", stored_hash.hex())

print("\nCorrect Password:",
      hasher.verify_password(password, salt, stored_hash))

print("Wrong Password:",
      hasher.verify_password("WrongPassword", salt, stored_hash))
