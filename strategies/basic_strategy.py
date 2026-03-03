import ta

class BasicStrategy:
    def generate_signal(self, df):
        df["rsi"] = ta.momentum.RSIIndicator(df["close"], window=14).rsi()
        df["sma"] = ta.trend.SMAIndicator(df["close"], window=20).sma_indicator()

        latest = df.iloc[-1]

        if latest["rsi"] < 30 and latest["close"] > latest["sma"]:
            return "BUY"
        elif latest["rsi"] > 70 and latest["close"] < latest["sma"]:
            return "SELL"
        else:
            return "HOLD"
