from abc import ABC, abstractmethod
class Vehicle(ABC):
    @abstractmethod
    def fuel_type(self):
        pass
    @abstractmethod
    def max_speed(self):
        pass
class BMW(Vehicle):
    def fuel_type(self):
        return "Diesel"
    def max_speed(self):
        return "240 km/h"
class Ferrari(Vehicle):
    def fuel_type(self):
        return "Petrol"
    def max_speed(self):
        return "350 km/h"
def car_details(car):
    print("Fuel: {}".format(car.fuel_type()))
    print("Max Speed: {}".format(car.max_speed()))
bmw_car = BMW()
ferrari_car = Ferrari()
print(" Vehicle Details")
for car in (bmw_car, ferrari_car):
    car_details(car)