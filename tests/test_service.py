import pytest
from services.carbon_service import CarbonService
from schemas.carbon_schema import CarbonRequest
from domain.enum.vehicle_type import VehicleType


service = CarbonService()


def test_distance_zero_returns_zero():
    data = CarbonRequest(
        vehicleType=VehicleType.DIESEL,
        distance=0.0001,
        weight=0.0001,
        efficiency=1
    )
    result = service.calculate(data)
    assert result >= 0


def test_valid_calculation_diesel():
    data = CarbonRequest(
        vehicleType=VehicleType.DIESEL,
        distance=100,
        weight=10,
        efficiency=2
    )
    result = service.calculate(data)
    assert result == 50.0


def test_valid_calculation_electric():
    data = CarbonRequest(
        vehicleType=VehicleType.ELECTRIC,
        distance=100,
        weight=10,
        efficiency=2
    )
    result = service.calculate(data)
    assert result == 10.0


def test_efficiency_zero_should_fail():
    with pytest.raises(Exception):
        CarbonRequest(
            vehicleType=VehicleType.DIESEL,
            distance=100,
            weight=10,
            efficiency=0
        )