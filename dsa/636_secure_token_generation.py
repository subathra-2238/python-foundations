import secrets
import string


class TokenGenerator:

    def generate_token(self, length=32):

        characters = string.ascii_letters + string.digits

        token = ''.join(
            secrets.choice(characters)
            for _ in range(length)
        )

        return token

    def verify_token(self, token, stored_token):

        return secrets.compare_digest(
            token,
            stored_token
        )


generator = TokenGenerator()

secure_token = generator.generate_token()

print("Generated Token:", secure_token)
print("Token Length:", len(secure_token))

print("\nCorrect Token:",
      generator.verify_token(secure_token, secure_token))

print("Incorrect Token:",
      generator.verify_token("wrong_token", secure_token))
