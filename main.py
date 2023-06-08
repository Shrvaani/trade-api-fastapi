from typing import List, Optional
from fastapi import FastAPI, Query, Body
from datetime import datetime
from pydantic import BaseModel
from database import Trade, MockDatabase

app = FastAPI()
mock_db = MockDatabase()


class TradeSearchFilters(BaseModel):
    search: Optional[str] = None
    instrument_id: Optional[int] = None
    asset_class: Optional[str] = None
    start: Optional[str] = None
    end: Optional[str] = None
    min_price: Optional[float] = None
    max_price: Optional[float] = None
    trade_type: Optional[str] = None


@app.get("/trades", response_model=List[Trade])
def get_trades(
    page: int = Query(1, ge=1),
    limit: int = Query(10, ge=1, le=100),
    sort_by: Optional[str] = Query(None, regex=r"^(id|instrumentId|instrumentName|tradeDateTime|tradeDetails\.price)$"),
    sort_desc: bool = Query(False),
    search_filters: TradeSearchFilters = Body(default=TradeSearchFilters()),
):
    trades = mock_db.get_trades(
        search=search_filters.search,
        instrument_id=search_filters.instrument_id,
        asset_class=search_filters.asset_class,
        start=search_filters.start,
        end=search_filters.end,
        min_price=search_filters.min_price,
        max_price=search_filters.max_price,
        trade_type=search_filters.trade_type,
    )

    # Sorting
    if sort_by:
        trades = sorted(trades, key=lambda t: getattr(t, sort_by), reverse=sort_desc)

    # Pagination
    start_index = (page - 1) * limit
    end_index = start_index + limit
    trades = trades[start_index:end_index]

    return trades


@app.get("/trades/{trade_id}", response_model=Trade)
def get_trade_by_id(trade_id: int):
    trade = mock_db.get_trade_by_id(trade_id)
    if not trade:
        raise HTTPException(status_code=404, detail="Trade not found")
    return trade
