class MessageFilter:

    def __init__(self):
        self.messages = []

    def add_message(self, message):
        self.messages.append(message)

    def filter_messages(self, keyword):

        print(f"\nFiltering messages for: {keyword}")

        found = False

        for message in self.messages:

            if keyword.lower() in message.lower():
                print(f"Matched: {message}")
                found = True

        if not found:
            print("No matching messages found")


filter_system = MessageFilter()

filter_system.add_message("AI workshop tomorrow")
filter_system.add_message("Robotics competition next week")
filter_system.add_message("AI project submission Friday")
filter_system.add_message("Cybersecurity seminar Monday")

filter_system.filter_messages("AI")
filter_system.filter_messages("Robotics")
