class MessageRouter:

    def __init__(self):
        self.routes = {}

    def add_route(self, destination, receiver):
        self.routes[destination] = receiver
        print(f"Route added: {destination} -> {receiver}")

    def send_message(self, destination, message):

        print(f"\nSending: {message}")

        receiver = self.routes.get(destination)

        if receiver:
            print(f"Delivered to: {receiver}")
        else:
            print(f"No route found for: {destination}")


router = MessageRouter()

router.add_route("AI", "AI Department")
router.add_route("Robotics", "Robotics Department")
router.add_route("IoT", "IoT Department")

router.send_message("AI", "New AI workshop announced")
router.send_message("IoT", "Sensor project update")
router.send_message("Cybersecurity", "Security seminar")
