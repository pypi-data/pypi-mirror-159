from enum import Enum, auto
from typing import Optional


class MARKET_TYPE(Enum):
    LIT_POOL = auto()
    DARK_POOL = auto()


class MARKET_EXECUTION(Enum):
    PRICE_TIME_PRIORITY = auto()
    PRO_RATA = auto()


class ORDER_SIDE(Enum):
    BUY = auto()
    SELL = auto()


class ORDER_TYPE(Enum):
    LIMIT = auto()
    MARKET = auto()


class BaseOrder:
    def __init__(
        self,
        ticker: str,
        oside: ORDER_SIDE,
        otype: ORDER_TYPE,
        qty: float,
        price: float,
    ) -> None:
        self.ticker = ticker
        self.oside = oside
        self.otype = otype
        self.qty = qty
        self.price = price


class PQN:
    def __init__(
        self,
        price: float,
        qty: float,
        num: Optional[int] = None,
    ) -> None:
        self.price = price
        self.qty = qty
        self.num = num


class LimitOrderBook:
    def __init__(
        self,
        timestamp: str,
        ticker: str,
        bid: list[PQN],
        ask: list[PQN],
    ) -> None:
        self.timestamp = timestamp
        self.ticker = ticker
        self.bid = bid
        self.ask = ask


class Price:
    def __init__(
        self,
        timestamp: str,
        ticker: str,
        trade: PQN,
        bid: Optional[PQN],
        ask: Optional[PQN],
    ) -> None:
        self.timestamp = timestamp
        self.ticker = ticker
        self.trade = trade
        self.bid = bid
        self.ask = ask
