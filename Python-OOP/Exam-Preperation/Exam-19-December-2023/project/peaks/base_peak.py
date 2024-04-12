from abc import ABC, abstractmethod


class BasePeak(ABC):
    recommended_gear = []

    def __init__(self, name: str, elevation: int):
        self.name = name
        self.elevation = elevation
        self.difficulty_level = BasePeak.calculate_difficulty_level()

    @staticmethod
    def raiser(ex):
        raise ex

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value if len(value) >= 2 \
            else BasePeak.raiser(ValueError("Peak name cannot be less than 2 symbols!"))

    @property
    def elevation(self):
        return self._elevation

    @elevation.setter
    def elevation(self, value):
        self._elevation = value if not value < 1500 \
            else BasePeak.raiser(ValueError("Peak elevation cannot be below 1500m."))

    @abstractmethod
    def calculate_difficulty_level(self):
        ...

    @abstractmethod
    def get_recommended_gear(self):
        ...




