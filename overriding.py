class vehicle:
    def start(self):
        print("is starting")
class car(vehicle):
    def start1(self):
        print("car is starting")
car=car()
car.start()