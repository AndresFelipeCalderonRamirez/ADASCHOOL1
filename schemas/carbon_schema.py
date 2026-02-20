from pydantic import BaseModel, Field, field_validator
from domain.enum.vehicle_type import VehicleType


class CarbonRequest(BaseModel):
    vehicleType: VehicleType
    distance: float = Field(gt=0, le=100000)
    weight: float = Field(gt=0, le=1000)
    efficiency: float = Field(gt=0, le=100)

    @field_validator("distance", "weight", "efficiency")
    @classmethod
    def must_be_finite(cls, value):
        if not float(value) == value or value == float("inf"):
            raise ValueError("Value must be finite")
        return value


class CarbonResponse(BaseModel):
    co2: float
    unit: str = "kg"