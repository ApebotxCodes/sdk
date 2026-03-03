from agents.trading_agent import TradingAgent
import time

if __name__ == "__main__":
    agent = TradingAgent()

    while True:
        try:
            agent.run()
            time.sleep(60)
        except Exception as e:
            print("Error:", e)
            time.sleep(10)
