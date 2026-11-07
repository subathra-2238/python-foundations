class MessageBroker:

    def __init__(self):
        self.subscribers = {}

    def subscribe(self, topic, receiver):

        if topic not in self.subscribers:
            self.subscribers[topic] = []

        self.subscribers[topic].append(receiver)

        print(f"{receiver} subscribed to {topic}")

    def publish(self, topic, message):

        print(f"\nPublishing to {topic}: {message}")

        if topic not in self.subscribers:
            print("No subscribers found")
            return

        for receiver in self.subscribers[topic]:
            print(f"Delivered to {receiver}")


broker = MessageBroker()

broker.subscribe("Sports", "Student A")
broker.subscribe("Sports", "Student B")
broker.subscribe("Technology", "Student C")

broker.publish("Sports", "Football match tomorrow")
broker.publish("Technology", "New AI workshop announced")
