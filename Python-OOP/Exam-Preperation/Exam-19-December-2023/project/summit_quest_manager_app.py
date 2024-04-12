from typing import List
from project.climbers.arctic_climber import ArcticClimber
from project.climbers.base_climber import BaseClimber
from project.climbers.summit_climber import SummitClimber
from project.peaks.arctic_peak import ArcticPeak
from project.peaks.base_peak import BasePeak
from project.peaks.summit_peak import SummitPeak


class SummitQuestManagerApp:

    def __init__(self):
        self.climbers: List[BaseClimber] = []
        self.peaks: List[BasePeak] = []

    def register_climber(self, climber_type: str, climber_name: str):
        climber_dict = {"ArcticClimber": ArcticClimber, "SummitClimber": SummitClimber}

        if climber_type in climber_dict:
            try:
                climber = next(filter(lambda c: c.name == climber_name, self.climbers))
                return f"{climber.name} has been already registered."
            except StopIteration:
                new_climber = climber_dict[climber_type](climber_name)
                self.climbers.append(new_climber)
                return f"{climber_name} is successfully registered as a {climber_type}."

        return f"{climber_type} doesn't exist in our register."

    def peak_wish_list(self, peak_type: str, peak_name: str, peak_elevation: int):
        peak_dict = {"ArcticPeak": ArcticPeak, "SummitPeak": SummitPeak}

        if peak_type in peak_dict:
            new_peak = peak_dict[peak_type](peak_name, peak_elevation)
            self.peaks.append(new_peak)
            return f"{peak_name} is successfully added to the wish list as a {peak_type}."

        return f"{peak_type} is an unknown type of peak."

    def check_gear(self, climber_name: str, peak_name: str, gear: List[str]):
        climber = next(filter(lambda c: c.name == climber_name, self.climbers))
        peak = next(filter(lambda p: p.name == peak_name, self.peaks))

        sorted_gear = sorted(gear)
        sorted_peak_gear = sorted(peak.get_recommended_gear())

        if sorted_gear == sorted_peak_gear:
            return f"{climber_name} is prepared to climb {peak_name}."

        climber.is_prepared = False

        return f"{climber_name} is not prepared to climb {peak_name}. " \
               f"Missing gear: {sorted_gear}."

    def perform_climbing(self, climber_name: str, peak_name: str):
        try:
            climber = next(filter(lambda c: c.name == climber_name, self.climbers))
        except StopIteration:
            return f"Climber {climber_name} is not registered yet."

        try:
            peak = next(filter(lambda p: p.name == peak_name, self.peaks))
        except StopIteration:
            return f"Peak {peak_name} is not part of the wish list."

        if climber.can_climb():
            if climber.is_prepared:
                return f"{climber_name} conquered {peak_name} whose difficulty level is {peak.difficulty_level}."
            return f"{climber_name} will need to be better prepared next time."
        else:
            return f"{climber_name} needs more strength to climb {peak_name} and is therefore taking some rest."

    def get_statistics(self):
        pass




