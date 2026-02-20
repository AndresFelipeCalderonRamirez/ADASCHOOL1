from fastapi import APIRouter, Depends
from schemas.carbon_schema import CarbonRequest, CarbonResponse
from services.carbon_service import CarbonService

router = APIRouter()
service = CarbonService()


@router.post("/calculate", response_model=CarbonResponse)
def calculate_carbon(payload: CarbonRequest):
    result = service.calculate(payload)
    return CarbonResponse(co2=result)