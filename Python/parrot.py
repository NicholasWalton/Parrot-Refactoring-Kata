from abc import ABC, abstractmethod


class Parrot(ABC):

    def __init__(self, voltage, nailed):
        self._voltage = voltage
        self._nailed = nailed

    def speed(self):
        return self._base_speed()

    @abstractmethod
    def cry(self): pass

    def _base_speed(self):
        return 12.0


class African(Parrot):
    def __init__(self, number_of_coconuts, voltage, nailed):
        super().__init__(voltage, nailed)
        self._number_of_coconuts = number_of_coconuts

    def speed(self):
        return max(0, self._base_speed() - self._load_factor() * self._number_of_coconuts)

    def cry(self):
        return "Sqaark!"

    def _load_factor(self):
        return 9.0


class European(Parrot):
    def __init__(self, voltage, nailed):
        super().__init__(voltage, nailed)

    def cry(self):
        return "Sqoork!"


class NorwegianBlue(Parrot):
    def __init__(self, voltage, nailed):
        super().__init__(voltage, nailed)

    def cry(self):
        return "Bzzzzzz" if self._voltage > 0 else "..."

    def speed(self):
        return 0 if self._nailed else self._compute_base_speed_for_voltage(self._voltage)

    def _compute_base_speed_for_voltage(self, voltage):
        return min([24.0, voltage * self._base_speed()])
