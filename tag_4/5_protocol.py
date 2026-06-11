"""
Protocol: via statischer Type-Prüfung,
"""

from typing import Protocol


class TradingStrategy(Protocol):
    def should_buy(self, prices: list[float]) -> bool: ...

    def should_sell(self, prices: list[float]) -> bool: ...


class MinMaxTradingStrategy:
    def should_buy(self, prices: list[float]) -> bool:
        return True

    def should_sell(self, prices: list[float]) -> bool:
        return True


def use_strategry(strategy: TradingStrategy, prices: list) -> None:
    # wenn strategy dass TradingStrategy-Protokoll nicht erfüllt, dann
    # beschwert sich der Type-checker
    print(strategy.should_buy(prices))


minmax: TradingStrategy = MinMaxTradingStrategy()
use_strategry(minmax, [0.1, 0.2])
