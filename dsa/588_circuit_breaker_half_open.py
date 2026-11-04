class CircuitBreaker:

    def __init__(self, failure_limit):
        self.failure_limit = failure_limit
        self.failures = 0
        self.state = "CLOSED"

    def call_service(self, success):

        if self.state == "OPEN":
            print("Request blocked!")
            return

        if success:
            print("Service call successful!")
            self.failures = 0
            self.state = "CLOSED"

        else:
            print("Service call failed!")
            self.failures += 1

            if self.failures >= self.failure_limit:
                self.state = "OPEN"

        print("State:", self.state)

    def allow_test_request(self):
        if self.state == "OPEN":
            self.state = "HALF-OPEN"
            print("Testing service recovery...")

    def show_state(self):
        print("Current State:", self.state)


breaker = CircuitBreaker(2)

breaker.call_service(False)
breaker.call_service(False)

breaker.allow_test_request()

breaker.call_service(True)

breaker.show_state()
