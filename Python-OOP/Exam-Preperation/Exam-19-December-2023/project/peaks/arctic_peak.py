from project.peaks.base_peak import BasePeak


class ArcticPeak(BasePeak):
    recommended_gear = ["Ice axe", "Crampons", "Insulated clothing", "Helmet"]

    def calculate_difficulty_level(self):
        if self.elevation > 3000:
            return "Extreme"
        elif 2000 <= self.elevation <= 3000:
            return "Advanced"

    def get_recommended_gear(self):
        return ArcticPeak.recommended_gear
