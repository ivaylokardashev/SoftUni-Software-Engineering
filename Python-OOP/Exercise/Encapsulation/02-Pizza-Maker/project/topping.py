from project.raiser import raiser


class Topping:

    def __init__(self, topping_type: str, weight: float):
        self.topping_type = topping_type
        self.weight = weight

    @property
    def topping_type(self):
        return self.__topping_type
    
    @topping_type.setter
    def topping_type(self, value):
        self.__topping_type = value if value != "" \
            else raiser(ValueError("The topping type cannot be an empty string"))

    @property
    def weight(self):
        return self.__weight

    @weight.setter
    def weight(self, value):
        self.__weight = value if value > 0 \
            else raiser(ValueError("The weight cannot be less or equal to zero"))





