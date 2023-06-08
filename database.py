from typing import List, Optional
from pydantic import BaseModel
from datetime import datetime


class TradeDetails(BaseModel):
    price: float
    quantity: int
    buySellIndicator: str


class TraderDetails(BaseModel):
    name: str
    address: str


class Trade(BaseModel):
    id: int
    instrumentId: int
    instrumentName: str
    tradeDateTime: str
    tradeDetails: TradeDetails
    traderDetails: TraderDetails


class MockDatabase:
    def __init__(self):
        self.trades_db = [
            Trade(
                id=1,
                instrumentId=1,
                instrumentName="Instrument 1",
                tradeDateTime=datetime.now().isoformat(),
                tradeDetails=TradeDetails(price=100.0, quantity=10, buySellIndicator="BUY"),
                traderDetails=TraderDetails(name="John Doe", address="123 Main St")
            ),
            Trade(
                id=2,
                instrumentId=2,
                instrumentName="Instrument 2",
                tradeDateTime=datetime.now().isoformat(),
                tradeDetails=TradeDetails(price=200.0, quantity=20, buySellIndicator="SELL"),
                traderDetails=TraderDetails(name="Jane Smith", address="456 Elm St")
            ),
            Trade(
                id=3,
                instrumentId=1,
                instrumentName="Instrument 1",
                tradeDateTime=datetime.now().isoformat(),
                tradeDetails=TradeDetails(price=150.0, quantity=15, buySellIndicator="BUY"),
                traderDetails=TraderDetails(name="Michael Johnson", address="789 Oak St")
            ),
        ]

    def get_trades(
        self,
        search: Optional[str] = None,
        instrument_id: Optional[int] = None,
        asset_class: Optional[str] = None,
        start: Optional[str] = None,
        end: Optional[str] = None,
        min_price: Optional[float] = None,
        max_price: Optional[float] = None,
        trade_type: Optional[str] = None,
    ) -> List[Trade]:
        filtered_trades = self.trades_db

        if search:
            search = search.lower()
            filtered_trades = [trade for trade in filtered_trades if self._trade_contains_text(trade, search)]

        if instrument_id:
            filtered_trades = [trade for trade in filtered_trades if trade.instrumentId == instrument_id]

        if asset_class:
            filtered_trades = [trade for trade in filtered_trades if trade.instrumentName.lower() == asset_class.lower()]

        if start:
            start_datetime = datetime.fromisoformat(start)
            filtered_trades = [trade for trade in filtered_trades if datetime.fromisoformat(trade.tradeDateTime) >= start_datetime]

        if end:
            end_datetime = datetime.fromisoformat(end)
            filtered_trades = [trade for trade in filtered_trades if datetime.fromisoformat(trade.tradeDateTime) <= end_datetime]

        if min_price:
            filtered_trades = [trade for trade in filtered_trades if trade.tradeDetails.price >= min_price]

        if max_price:
            filtered_trades = [trade for trade in filtered_trades if trade.tradeDetails.price <= max_price]

        if trade_type:
            filtered_trades = [trade for trade in filtered_trades if trade.tradeDetails.buySellIndicator.lower() == trade_type.lower()]

        return filtered_trades

    def _trade_contains_text(self, trade: Trade, text: str) -> bool:
        trade_text = (
            str(trade.id)
            + str(trade.instrumentId)
            + trade.instrumentName.lower()
            + trade.traderDetails.name.lower()
        )
        return text in trade_text

    def get_trade_by_id(self, trade_id: int) -> Optional[Trade]:
        for trade in self.trades_db:
            if trade.id == trade_id:
                return trade
        return None

mock_db = MockDatabase()
