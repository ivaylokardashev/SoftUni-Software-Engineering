from abc import ABC, abstractmethod


class Vehicle(ABC):

    def __init__(self, fuel_quantity: float, fuel_consumption: float):
        self.fuel_quantity = fuel_quantity
        self.fuel_consumption = fuel_consumption

    @abstractmethod
    def drive(self, distance: float):
        ...

    @abstractmethod
    def refuel(self, fuel: float):
        ...


class Car(Vehicle):
    CONDITIONER_CONSUMPTION = 0.9

    def drive(self, distance: float):
        consumption = (self.CONDITIONER_CONSUMPTION + self.fuel_consumption) * distance

        if self.fuel_quantity - consumption >= 0:
            self.fuel_quantity -= consumption

    def refuel(self, fuel: float):
        self.fuel_quantity += fuel


class Truck(Vehicle):
    CONDITIONER_CONSUMPTION = 1.6
    TINY_HOLE = 0.05

    def drive(self, distance: float):
        consumption = (self.CONDITIONER_CONSUMPTION + self.fuel_consumption) * distance

        if self.fuel_quantity - consumption >= 0:
            self.fuel_quantity -= consumption

    def refuel(self, fuel: float):
        self.fuel_quantity += fuel - (fuel * Truck.TINY_HOLE)


car = Car(20, 5)
car.drive(3)
print(car.fuel_quantity)
car.refuel(10)
print(car.fuel_quantity)


