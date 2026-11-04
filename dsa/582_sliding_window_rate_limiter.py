from collections import defaultdict, deque


class SlidingWindowRateLimiter:

    def __init__(self, limit, window_size):
        self.limit = limit
        self.window_size = window_size
        self.requests = defaultdict(deque)

    def allow_request(self, user, current_time):

        user_requests = self.requests[user]

        while user_requests and current_time - user_requests[0] >= self.window_size:
            user_requests.popleft()

        if len(user_requests) < self.limit:
            user_requests.append(current_time)
            return True

        return False


limiter = SlidingWindowRateLimiter(3, 10)

for timestamp in [1, 2, 3, 4, 12, 13]:
    result = limiter.allow_request("Subathra", timestamp)

    print(f"Time {timestamp}: {'Allowed' if result else 'Blocked'}")
