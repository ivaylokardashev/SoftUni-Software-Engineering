from project.animal import Animal


class Tiger(Animal):
    TIGER_CARE_COST = 45

    def __init__(self, name: str, gender: str, age: int):
        super().__init__(name, gender, age, self.TIGER_CARE_COST)