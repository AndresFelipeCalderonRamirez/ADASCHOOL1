from enum import Enum


class VehicleType(str, Enum):
    ELECTRIC = "ELECTRIC"
    DIESEL = "DIESEL"
    HYBRID = "HYBRID"