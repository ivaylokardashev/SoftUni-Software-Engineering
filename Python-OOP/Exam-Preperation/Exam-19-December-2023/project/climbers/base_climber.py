import math
from abc import ABC, abstractmethod
from project.peaks.base_peak import BasePeak


class BaseClimber(ABC):
    NEEDED_STRENGTH = 0
    CLIMBER_STRENGTH = 0
    EXTREME_VALUE_PEAK = 0
    ADVANCED_VALUE_PEAK = 0
    VALUE_FOR_CLIMB = 0

    def __init__(self, name: str, strength: float):
        self.name = name
        self.strength = strength
        self.is_prepared: bool = True
        self.conquered_peaks = []

    @staticmethod
    def raiser(ex):
        raise ex

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value if value.strip() != "" \
            else BaseClimber.raiser(ValueError("Climber name cannot be null or empty!"))

    @property
    def strength(self):
        return self._strength

    @strength.setter
    def strength(self, value):
        self._strength = value if value > 0 \
            else BaseClimber.raiser(ValueError("A climber cannot have negative strength or strength equal to 0!"))

    @abstractmethod
    def can_climb(self):
        ...

    @abstractmethod
    def climb(self, peak : BasePeak):
        ...

    def rest(self):
        self.strength += 15

    def __str__(self):
        return f"{self.__class__.name}: /// Climber name: {self.name} * Left strength: {math.ceil(self.strength)} " \
               f"* Conquered peaks: {', '.join(c for c in self.conquered_peaks)} ///"



