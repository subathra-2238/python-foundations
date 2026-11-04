class CircuitBreaker:

    def __init__(self, failure_limit):
        self.failure_limit = failure_limit
        self.failures = 0
        self.state = "CLOSED"

    def call_service(self, success):

        if self.state == "OPEN":
            print("Request blocked! Circuit is OPEN.")
            return

        if success:
            print("Service call successful!")
            self.failures = 0

        else:
            self.failures += 1
            print("Service call failed!")

        if self.failures >= self.failure_limit:
            self.state = "OPEN"
            print("Circuit breaker activated!")

        print("Circuit State:", self.state)


breaker = CircuitBreaker(3)

breaker.call_service(False)
breaker.call_service(False)
breaker.call_service(False)
breaker.call_service(True)
