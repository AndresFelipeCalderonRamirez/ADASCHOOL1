import pytest
from domain.strategies.electric_strategy import ElectricStrategy
from domain.strategies.diesel_strategy import DieselStrategy
from domain.strategies.hybrid_strategy import HybridStrategy


def test_electric_strategy():
    strategy = ElectricStrategy()
    result = strategy.calculate(100, 10, 2)
    assert result == (100 * 10 * 0.02) / 2


def test_diesel_strategy():
    strategy = DieselStrategy()
    result = strategy.calculate(100, 10, 2)
    assert result == (100 * 10 * 0.1) / 2


def test_hybrid_strategy():
    strategy = HybridStrategy()
    result = strategy.calculate(100, 10, 2)
    assert result == (100 * 10 * 0.05) / 2