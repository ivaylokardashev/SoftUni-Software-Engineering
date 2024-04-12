from project.divers.base_diver import BaseDiver


class FreeDiver(BaseDiver):
    INITIAL_OXYGEN_LEVEL = 120

    def __init__(self, name: str, oxygen_level: float):
        super().__init__(name, oxygen_level)

    def miss(self, time_to_catch: int):
        return None

    def renew_oxy(self):
        return None

