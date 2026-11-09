import secrets
import time


class OTPValidator:

    def generate_otp(self):

        otp = ''.join(
            str(secrets.randbelow(10))
            for _ in range(6)
        )

        expiry_time = time.time() + 30

        return otp, expiry_time

    def verify_otp(self, entered_otp, original_otp, expiry_time):

        if time.time() > expiry_time:
            return "OTP has expired!"

        if secrets.compare_digest(entered_otp, original_otp):
            return "OTP verified successfully!"

        return "Invalid OTP!"


validator = OTPValidator()

otp, expiry = validator.generate_otp()

print("Generated OTP:", otp)
print("Validity: 30 seconds")

print("\nCorrect OTP:")
print(validator.verify_otp(otp, otp, expiry))

print("\nIncorrect OTP:")
print(validator.verify_otp("000000", otp, expiry))

print("\nExpired OTP:")
print(validator.verify_otp(otp, otp, time.time() - 1))
