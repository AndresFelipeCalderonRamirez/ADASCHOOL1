from abc import ABC, abstractmethod


class EmissionStrategy(ABC):

    @abstractmethod
    def calculate(self, distance: float, weight: float, efficiency: float) -> float:
        pass