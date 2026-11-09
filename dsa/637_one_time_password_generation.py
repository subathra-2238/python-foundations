import secrets


class OTPGenerator:

    def generate_otp(self, length=6):

        return ''.join(
            str(secrets.randbelow(10))
            for _ in range(length)
        )

    def verify_otp(self, entered_otp, original_otp):

        return secrets.compare_digest(
            entered_otp,
            original_otp
        )


generator = OTPGenerator()

otp = generator.generate_otp()

print("Generated OTP:", otp)
print("OTP Length:", len(otp))

print("\nCorrect OTP:",
      generator.verify_otp(otp, otp))

print("Incorrect OTP:",
      generator.verify_otp("000000", otp))
