from domain.enum.vehicle_type import VehicleType
from domain.strategies.electric_strategy import ElectricStrategy
from domain.strategies.diesel_strategy import DieselStrategy
from domain.strategies.hybrid_strategy import HybridStrategy
from errors.custom_exceptions import ValidationException


class StrategyFactory:

    @staticmethod
    def create(vehicle_type: VehicleType):
        if vehicle_type == VehicleType.ELECTRIC:
            return ElectricStrategy()
        elif vehicle_type == VehicleType.DIESEL:
            return DieselStrategy()
        elif vehicle_type == VehicleType.HYBRID:
            return HybridStrategy()
        else:
            raise ValidationException("Invalid vehicle type")