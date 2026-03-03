class Executor:
    def execute_trade(self, exchange, signal, symbol, amount):
        if signal == "BUY":
            order = exchange.create_market_buy_order(symbol, amount)
        elif signal == "SELL":
            order = exchange.create_market_sell_order(symbol, amount)
        else:
            return None

        return order
