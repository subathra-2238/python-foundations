import time


class TokenBucket:

    def __init__(self, capacity, refill_rate):
        self.capacity = capacity
        self.tokens = capacity
        self.refill_rate = refill_rate
        self.last_refill = time.time()

    def allow_request(self):

        current_time = time.time()

        elapsed = current_time - self.last_refill

        new_tokens = elapsed * self.refill_rate

        self.tokens = min(
            self.capacity,
            self.tokens + new_tokens
        )

        self.last_refill = current_time

        if self.tokens >= 1:
            self.tokens -= 1
            return True

        return False


bucket = TokenBucket(3, 1)

for i in range(5):
    result = bucket.allow_request()

    print(f"Request {i + 1}: {'Allowed' if result else 'Blocked'}")
