from abstractvehicle import AbstractVehicle

class bike(AbstractVehicle):
    def display_details(self):
        print("Bike Details")
        print(f"Color:{self.color}")
        print(f"number of tyres:{self.num_tyre}")
        print(f"Gears:{self.gears}")

class car(AbstractVehicle):
    def display_details(self):
        print("car Details")
        print(f"Color:{self.color}")
        print(f"number of tyres:{self.num_tyre}")
        print(f"Gears:{self.gears}")
        
class scooty(AbstractVehicle):
    def display_details(self):
        print("scooty Details")
        print(f"Color:{self.color}")
        print(f"number of tyres:{self.num_tyre}")
        print(f"Gears:{self.gears}")