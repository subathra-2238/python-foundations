class Engine:
    def start(self):
        print("Engine started.")


class Car:
    def __init__(self):
        self.engine = Engine()

    def start_car(self):
        self.engine.start()
        print("Car started.")


car1 = Car()

car1.start_car()