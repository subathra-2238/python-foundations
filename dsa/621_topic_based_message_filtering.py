class MessageBroker:

    def __init__(self):
        self.subscribers = {}

    def subscribe(self, topic, receiver):

        self.subscribers.setdefault(topic, []).append(receiver)

        print(f"{receiver} subscribed to {topic}")

    def publish(self, topic, message):

        print(f"\nNew message on {topic}: {message}")

        receivers = self.subscribers.get(topic, [])

        if not receivers:
            print("No matching subscribers")
            return

        for receiver in receivers:
            print(f"Delivered to: {receiver}")


broker = MessageBroker()

broker.subscribe("AI", "Student A")
broker.subscribe("Robotics", "Student B")
broker.subscribe("AI", "Student C")

broker.publish("AI", "New AI workshop announced")
broker.publish("Robotics", "Robotics competition tomorrow")
broker.publish("Cybersecurity", "Security awareness session")
