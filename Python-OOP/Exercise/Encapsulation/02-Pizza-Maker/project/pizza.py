from project.dough import Dough
from project.topping import Topping
from project.raiser import raiser


class Pizza:

    def __init__(self, name: str, dough: Dough, max_number_of_toppings: int):
        self.name = name
        self.dough = dough
        self.max_number_of_toppings = max_number_of_toppings
        self.toppings = {}

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value if value != "" \
            else raiser(ValueError("The name cannot be an empty string"))

    @property
    def dough(self):
        return self.__dough

    @dough.setter
    def dough(self, value):
        self.__dough = value if value is not None \
            else raiser(ValueError("You should add dough to the pizza"))

    @property
    def max_number_of_toppings(self):
        return self.__max_number_of_toppings

    @max_number_of_toppings.setter
    def max_number_of_toppings(self, value):
        self.__max_number_of_toppings = value if value > 0 \
            else raiser(ValueError("The maximum number of toppings cannot be less or equal to zero"))

    def add_topping(self, topping: Topping):
        if len(self.toppings.keys()) >= self.max_number_of_toppings:
            raiser((ValueError("Not enough space for another topping")))
        if self.toppings.get(topping.topping_type):
            self.toppings[topping.topping_type] += topping.weight
        else:
            self.toppings[topping.topping_type] = topping.weight

    def calculate_total_weight(self):
        total_weight = self.dough.weight + sum(self.toppings.values())
        return total_weight




