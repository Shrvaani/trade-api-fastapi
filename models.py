import datetime as dt

from typing import Optional
from pydantic import BaseModel, Field


class TradeDetails(BaseModel):
    traderId: int
    quantity: int
    price: float

class Trade(BaseModel):
    id: int
    instrumentId: int
    instrumentName: str
    tradeDateTime: str
    tradeDetails: TradeDetails
