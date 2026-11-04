import time


class CircuitBreaker:

    def __init__(self, failure_limit, recovery_timeout):
        self.failure_limit = failure_limit
        self.recovery_timeout = recovery_timeout
        self.failures = 0
        self.state = "CLOSED"
        self.opened_at = None

    def call_service(self, success):

        if self.state == "OPEN":

            if time.time() - self.opened_at >= self.recovery_timeout:
                self.state = "HALF-OPEN"
                print("Testing service recovery...")
            else:
                print("Request blocked!")
                return

        if success:
            print("Service call successful!")
            self.failures = 0
            self.state = "CLOSED"
            self.opened_at = None

        else:
            print("Service call failed!")
            self.failures += 1

            if self.failures >= self.failure_limit:
                self.state = "OPEN"
                self.opened_at = time.time()
                print("Circuit breaker activated!")

        print("State:", self.state)


breaker = CircuitBreaker(2, 3)

breaker.call_service(False)
breaker.call_service(False)

time.sleep(3)

breaker.call_service(True)
