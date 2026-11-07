class MessageBroadcaster:

    def __init__(self):
        self.subscribers = []

    def subscribe(self, receiver):
        self.subscribers.append(receiver)
        print(f"{receiver} subscribed")

    def broadcast(self, message):

        print(f"\nBroadcasting: {message}")

        for receiver in self.subscribers:
            print(f"Delivered to: {receiver}")


broadcaster = MessageBroadcaster()

broadcaster.subscribe("Student A")
broadcaster.subscribe("Student B")
broadcaster.subscribe("Student C")

broadcaster.broadcast("College event starts at 10 AM")
