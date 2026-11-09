import secrets
import time


class SessionManager:

    def __init__(self):

        self.sessions = {}

    def create_session(self, username):

        session_id = secrets.token_urlsafe(32)

        self.sessions[session_id] = {
            "username": username,
            "created_at": time.time()
        }

        return session_id

    def validate_session(self, session_id):

        if session_id in self.sessions:

            username = self.sessions[session_id]["username"]

            print("Session valid!")
            print("Welcome:", username)

        else:

            print("Invalid session!")

    def destroy_session(self, session_id):

        if session_id in self.sessions:

            del self.sessions[session_id]

            print("Session terminated!")

        else:

            print("Session not found!")


manager = SessionManager()

# Create session
session = manager.create_session("Subathra")

print("Session ID:", session)

# Validate session
print("\nValidating Session:")
manager.validate_session(session)

# Destroy session
print("\nLogging Out:")
manager.destroy_session(session)

# Validate again
print("\nChecking Session Again:")
manager.validate_session(session)
