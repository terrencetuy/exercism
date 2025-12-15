from enum import Enum 


class OrbitalPeriods(Enum):
    MERCURY = 0.2408467
    VENUS = 0.61519726
    EARTH = 1
    MARS = 1.8808158
    JUPITER = 11.862615
    SATURN = 29.447498
    URANUS = 84.016846
    NEPTUNE = 164.79132


class SpaceAge:
    def __init__(self, seconds):
        self.years = seconds/(60*60*24*365.25)
        for period in OrbitalPeriods:
            setattr(self, "on_" + period.name.lower(), self._age(period))

        
    def _age(self, orbital_period):
        return lambda orbital_period=orbital_period: round(self.years/orbital_period.value, 2)
    