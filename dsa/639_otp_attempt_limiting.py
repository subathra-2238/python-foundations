import secrets


class OTPAttemptLimiter:

    def __init__(self, max_attempts=3):

        self.max_attempts = max_attempts
        self.attempts = 0
        self.otp = self.generate_otp()

    def generate_otp(self):

        return ''.join(
            str(secrets.randbelow(10))
            for _ in range(6)
        )

    def verify_otp(self, entered_otp):

        if self.attempts >= self.max_attempts:
            return "Account temporarily locked!"

        if secrets.compare_digest(entered_otp, self.otp):
            return "OTP verified successfully!"

        self.attempts += 1

        remaining = self.max_attempts - self.attempts

        if remaining == 0:
            return "Maximum attempts reached!"

        return f"Incorrect OTP! Attempts remaining: {remaining}"


validator = OTPAttemptLimiter()

print("Generated OTP:", validator.otp)

print("\nAttempt 1:")
print(validator.verify_otp("111111"))

print("\nAttempt 2:")
print(validator.verify_otp("222222"))

print("\nAttempt 3:")
print(validator.verify_otp("333333"))

print("\nAttempt 4:")
print(validator.verify_otp("444444"))
