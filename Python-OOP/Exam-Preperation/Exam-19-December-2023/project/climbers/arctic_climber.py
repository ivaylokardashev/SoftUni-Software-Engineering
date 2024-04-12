from project.climbers.base_climber import BaseClimber
from project.peaks.base_peak import BasePeak


class ArcticClimber(BaseClimber):
    NEEDED_STRENGTH = 100
    CLIMBER_STRENGTH = 200
    EXTREME_VALUE_PEAK = 2
    ADVANCED_VALUE_PEAK = 1.5
    VALUE_FOR_CLIMB = 20

    def __init__(self, name: str):
        super().__init__(name, ArcticClimber.CLIMBER_STRENGTH)

    def can_climb(self):
        if self.strength >= ArcticClimber.NEEDED_STRENGTH:
            return True

        return False

    def climb(self, peak: BasePeak):
        self.strength -= ArcticClimber.VALUE_FOR_CLIMB * ArcticClimber.EXTREME_VALUE_PEAK if peak.difficulty_level == "Extreme" \
            else ArcticClimber.VALUE_FOR_CLIMB * ArcticClimber.ADVANCED_VALUE_PEAK

        self.conquered_peaks.append(peak.name)


