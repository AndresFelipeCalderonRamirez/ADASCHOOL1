from .base_strategy import EmissionStrategy


class DieselStrategy(EmissionStrategy):
    _factor_base = 0.1

    def calculate(self, distance: float, weight: float, efficiency: float) -> float:
        return (distance * weight * self._factor_base) / efficiency