from config import RISK_PER_TRADE

class RiskManager:
    def calculate_position_size(self, balance, price):
        risk_amount = balance * RISK_PER_TRADE
        position_size = risk_amount / price
        return position_size
