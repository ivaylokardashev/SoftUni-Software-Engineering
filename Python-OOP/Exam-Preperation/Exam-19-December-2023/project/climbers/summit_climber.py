from project.climbers.base_climber import BaseClimber
from project.peaks.base_peak import BasePeak


class SummitClimber(BaseClimber):
    CLIMBER_STRENGTH = 150
    NEEDED_STRENGTH = 75
    EXTREME_VALUE_PEAK = 2.5
    ADVANCED_VALUE_PEAK = 1.3
    VALUE_FOR_CLIMB = 30

    def __init__(self, name: str):
        super().__init__(name, SummitClimber.CLIMBER_STRENGTH)

    def can_climb(self):
        if self.strength >= SummitClimber.NEEDED_STRENGTH:
            return True

        return False

    def climb(self, peak: BasePeak):
        self.strength -= SummitClimber.VALUE_FOR_CLIMB * SummitClimber.ADVANCED_VALUE_PEAK \
            if peak.difficulty_level == "Advanced" \
            else SummitClimber.VALUE_FOR_CLIMB * SummitClimber.EXTREME_VALUE_PEAK
