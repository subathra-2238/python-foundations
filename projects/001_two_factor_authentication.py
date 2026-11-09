import secrets


class TwoFactorAuthentication:

    def __init__(self):
        self.password = "Python@123"
        self.otp = None

    def verify_password(self, entered_password):

        return secrets.compare_digest(
            entered_password,
            self.password
        )

    def generate_otp(self):

        self.otp = ''.join(
            str(secrets.randbelow(10))
            for _ in range(6)
        )

        return self.otp

    def verify_otp(self, entered_otp):

        if self.otp is None:
            return False

        if secrets.compare_digest(entered_otp, self.otp):
            self.otp = None
            return True

        return False


auth = TwoFactorAuthentication()

# First factor: Password
entered_password = "Python@123"

if auth.verify_password(entered_password):

    print("Password verified!")

    # Second factor: OTP
    generated_otp = auth.generate_otp()

    print("Generated OTP:", generated_otp)

    entered_otp = generated_otp

    if auth.verify_otp(entered_otp):
        print("OTP verified!")
        print("Login successful!")
    else:
        print("Invalid OTP!")

else:
    print("Incorrect password!")
    print("Login failed!")
