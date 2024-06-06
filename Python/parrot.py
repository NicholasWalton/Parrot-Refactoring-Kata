from abc import ABC, abstractmethod


class Parrot(ABC):
    def speed(self):
        return self._base_speed()

    @abstractmethod
    def cry(self): pass

    def _base_speed(self):
        return 12.0


class African(Parrot):
    _LOAD_FACTOR = 9.0

    def __init__(self, number_of_coconuts):
        self._number_of_coconuts = number_of_coconuts

    def speed(self):
        return max(0, self._base_speed() - self._speed_reduction())

    def _speed_reduction(self):
        return self._LOAD_FACTOR * self._number_of_coconuts

    def cry(self):
        return "Sqaark!"


class European(Parrot):
    def cry(self):
        return "Sqoork!"


class NorwegianBlue(Parrot):
    def __init__(self, voltage):
        self._voltage = voltage

    def speed(self):
        return min([24.0, self._voltage * self._base_speed()])

    def cry(self):
        return "Bzzzzzz" if self._voltage > 0 else "..."


class Nailed(NorwegianBlue):

    def speed(self):
        return 0
