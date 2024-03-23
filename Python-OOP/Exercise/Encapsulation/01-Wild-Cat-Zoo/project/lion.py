from project.animal import Animal


class Lion(Animal):
    LION_CARE_COST = 50

    def __init__(self, name: str, gender: str, age: int):
        super().__init__(name, gender, age, self.LION_CARE_COST)