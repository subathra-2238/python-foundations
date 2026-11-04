import time


class LeakyBucket:

    def __init__(self, capacity, leak_rate):
        self.capacity = capacity
        self.leak_rate = leak_rate
        self.water = 0
        self.last_time = time.time()

    def add_request(self):

        current_time = time.time()

        elapsed = current_time - self.last_time

        leaked = elapsed * self.leak_rate

        self.water = max(0, self.water - leaked)

        self.last_time = current_time

        if self.water < self.capacity:
            self.water += 1
            return True

        return False


bucket = LeakyBucket(3, 1)

for i in range(5):
    result = bucket.add_request()

    print(
        f"Request {i + 1}: "
        f"{'Accepted' if result else 'Rejected'}"
    )
