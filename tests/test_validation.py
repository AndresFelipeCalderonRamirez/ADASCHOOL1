import pytest
from pydantic import ValidationError
from schemas.carbon_schema import CarbonRequest
from domain.enum.vehicle_type import VehicleType


def test_negative_weight():
    with pytest.raises(ValidationError):
        CarbonRequest(
            vehicleType=VehicleType.DIESEL,
            distance=100,
            weight=-5,
            efficiency=2
        )


def test_invalid_vehicle_type():
    with pytest.raises(ValidationError):
        CarbonRequest(
            vehicleType="PLANE",
            distance=100,
            weight=10,
            efficiency=2
        )


def test_infinite_value():
    with pytest.raises(ValidationError):
        CarbonRequest(
            vehicleType=VehicleType.DIESEL,
            distance=float("inf"),
            weight=10,
            efficiency=2
        )