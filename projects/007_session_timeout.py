import secrets
import time


class SessionManager:

    def __init__(self, timeout=10):

        self.sessions = {}
        self.timeout = timeout

    def create_session(self, username):

        session_id = secrets.token_urlsafe(16)

        self.sessions[session_id] = {
            "username": username,
            "last_activity": time.time()
        }

        return session_id

    def validate_session(self, session_id):

        if session_id not in self.sessions:
            print("Invalid session!")
            return False

        session = self.sessions[session_id]

        elapsed = time.time() - session["last_activity"]

        if elapsed >= self.timeout:

            del self.sessions[session_id]

            print("Session expired!")
            print("Automatically logged out!")

            return False

        session["last_activity"] = time.time()

        print("Session active!")
        print("Welcome:", session["username"])

        return True


manager = SessionManager(timeout=10)

session = manager.create_session("Subathra")

print("Session created!")

print("\nChecking session:")
manager.validate_session(session)

print("\nWaiting for 11 seconds...")
time.sleep(11)

print("\nChecking session again:")
manager.validate_session(session)
