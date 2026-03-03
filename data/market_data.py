import ccxt
import pandas as pd
from config import EXCHANGE, API_KEY, API_SECRET, SYMBOL, TIMEFRAME

class MarketData:
    def __init__(self):
        exchange_class = getattr(ccxt, EXCHANGE)
        self.exchange = exchange_class({
            "apiKey": API_KEY,
            "secret": API_SECRET,
            "enableRateLimit": True
        })

    def fetch_ohlcv(self, limit=100):
        ohlcv = self.exchange.fetch_ohlcv(SYMBOL, TIMEFRAME, limit=limit)
        df = pd.DataFrame(
            ohlcv,
            columns=["timestamp", "open", "high", "low", "close", "volume"]
        )
        return df
