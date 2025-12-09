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
        #self.orbital_per
        
    def on_earth(self):
        return self._age(OrbitalPeriods.EARTH)

    def on_mercury(self):
        return self._age(OrbitalPeriods.MERCURY)

    def on_venus(self):
        return self._age(OrbitalPeriods.VENUS)

    def on_mars(self):
        return self._age(OrbitalPeriods.MARS)

    def on_jupiter(self):
        return self._age(OrbitalPeriods.JUPITER)
        
    def on_saturn(self):
        return self._age(OrbitalPeriods.SATURN)

    def on_uranus(self):
        return self._age(OrbitalPeriods.URANUS)

    def on_neptune(self):
        return self._age(OrbitalPeriods.NEPTUNE)
        
    def _age(self, orbital_period):
        return round(self.years/orbital_period.value, 2)
    