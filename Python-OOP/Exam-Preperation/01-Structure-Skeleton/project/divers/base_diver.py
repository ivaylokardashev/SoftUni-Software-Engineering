from abc import ABC, abstractmethod
from project.fish.base_fish import BaseFish


class BaseDiver(ABC):

    def __init__(self, name: str, oxygen_level: float):
        self.name = name
        self.oxygen_level = oxygen_level
        self.catch: list = []
        self.competition_points = self.rounded_points
        self.has_health_issue: bool = False


    @property
    def rounded_points(self):
        return round(sum(sum(f.points) for f in self.catch), 1)

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if value.strip() == "":
            raise ValueError("Diver name cannot be null or empty!")
        
        self.__name = value

    @property
    def oxygen_level(self):
        return self.__oxygen_level
    
    @oxygen_level.setter
    def oxygen_level(self, value):
        if value < 0:
            raise ValueError("Cannot create diver with negative oxygen level!")

        self.__oxygen_level = value

    @abstractmethod
    def miss(self, time_to_catch: int):
        pass

    @abstractmethod
    def renew_oxy(self):
        pass

    def hit(self, fish: BaseFish):
        return None

    def update_health_status(self):
        return None

    def __str__(self):
        return None