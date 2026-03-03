from data.market_data import MarketData
from strategies.basic_strategy import BasicStrategy
from risk.risk_manager import RiskManager
from execution.executor import Executor
from config import SYMBOL

class TradingAgent:
    def __init__(self):
        self.market_data = MarketData()
        self.strategy = BasicStrategy()
        self.risk_manager = RiskManager()
        self.executor = Executor()
        self.exchange = self.market_data.exchange

    def run(self):
        df = self.market_data.fetch_ohlcv()
        signal = self.strategy.generate_signal(df)

        print(f"[AI] Signal: {signal}")

        if signal != "HOLD":
            balance = self.exchange.fetch_balance()["free"]["USDT"]
            price = df["close"].iloc[-1]
            amount = self.risk_manager.calculate_position_size(balance, price)

            order = self.executor.execute_trade(
                self.exchange,
                signal,
                SYMBOL,
                amount
            )

            print("[EXECUTION] Order:", order)
