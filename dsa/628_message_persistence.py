import json
import os


class MessageStorage:

    def __init__(self, filename):
        self.filename = filename

    def save_message(self, message):

        messages = []

        if os.path.exists(self.filename):
            with open(self.filename, "r") as file:
                messages = json.load(file)

        messages.append(message)

        with open(self.filename, "w") as file:
            json.dump(messages, file, indent=4)

        print(f"Saved: {message}")

    def load_messages(self):

        if not os.path.exists(self.filename):
            print("No stored messages")
            return

        with open(self.filename, "r") as file:
            messages = json.load(file)

        print("\nStored Messages:")

        for message in messages:
            print(message)


storage = MessageStorage("messages.json")

storage.save_message("Order 101")
storage.save_message("Payment 102")
storage.save_message("Order 103")

storage.load_messages()
