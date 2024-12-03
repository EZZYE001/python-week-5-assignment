# Activity 2:

# Base class
class Vehicle:
    def move(self):
        raise NotImplementedError("Subclasses must implement this method")

# Subclass 1
class Car(Vehicle):
    def move(self):
        print("Driving 🚗")

# Subclass 2
class Plane(Vehicle):
    def move(self):
        print("Flying ✈️")

# Subclass 3
class Boat(Vehicle):
    def move(self):
        print("Sailing 🚤")

# Demonstrate polymorphism
def test_movement(vehicle):
    vehicle.move()

# Create instances
car = Car()
plane = Plane()
boat = Boat()

# Test their movements
test_movement(car)    # Output: Driving 🚗
test_movement(plane)  # Output: Flying ✈️
test_movement(boat)   # Output: Sailing 🚤
