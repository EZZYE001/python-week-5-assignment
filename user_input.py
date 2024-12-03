# Base class
class Smartphone:
    def __init__(self, brand, model, battery):
        self.brand = brand
        self.model = model
        self.battery = battery

    def call(self, number):
        if self.battery > 5:
            print(f"Calling {number} using {self.brand} {self.model}...")
            self.battery -= 5
        else:
            print("Battery too low to make a call!")

    def charge(self):
        self.battery = 100
        print(f"{self.brand} {self.model} is now fully charged.")

# Subclass
class Smartwatch(Smartphone):
    def __init__(self, brand, model, battery, strap_material):
        super().__init__(brand, model, battery)
        self.strap_material = strap_material

    def track_steps(self):
        print(f"Tracking steps on {self.brand} smartwatch!")

# Create objects and demonstrate functionality
phone = Smartphone("Apple", "iPhone 14", 50)
phone.call("123-456-7890")
phone.charge()

watch = Smartwatch("Samsung", "Galaxy Watch 5", 30, "Silicone")
watch.call("987-654-3210")  # Inherits call() method
watch.track_steps()
