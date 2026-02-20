from schemas.carbon_schema import CarbonRequest
from domain.factory.strategy_factory import StrategyFactory
from errors.custom_exceptions import InternalException


class CarbonService:

    def calculate(self, data: CarbonRequest) -> float:

        if data.distance == 0 or data.weight == 0:
            return 0.0

        strategy = StrategyFactory.create(data.vehicleType)

        result = strategy.calculate(
            data.distance,
            data.weight,
            data.efficiency
        )

        if not float("-inf") < result < float("inf"):
            raise InternalException("Calculation overflow")

        return round(result, 4)