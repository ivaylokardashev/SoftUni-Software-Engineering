from project.divers.base_diver import BaseDiver


class ScubaDiver(BaseDiver):
    INITIAL_OXYGEN_LEVEL = 540

    def __init__(self, name: str, oxygen_level: float):
        super().__init__(name, oxygen_level)

    def miss(self, time_to_catch: int):
        return None

    def renew_oxy(self):
        return None
