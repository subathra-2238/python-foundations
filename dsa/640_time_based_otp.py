import time
import hmac
import hashlib
import struct
import secrets


class TOTPGenerator:

    def __init__(self):
        self.secret = secrets.token_bytes(20)

    def generate_totp(self):

        time_counter = int(time.time()) // 30

        message = struct.pack(">Q", time_counter)

        hash_value = hmac.new(
            self.secret,
            message,
            hashlib.sha1
        ).digest()

        offset = hash_value[-1] & 0x0F

        code = struct.unpack(
            ">I",
            hash_value[offset:offset + 4]
        )[0] & 0x7FFFFFFF

        return str(code % 1000000).zfill(6)


generator = TOTPGenerator()

otp = generator.generate_totp()

print("Generated TOTP:", otp)
print("Validity: 30 seconds")
print("Current OTP:", generator.generate_totp())
