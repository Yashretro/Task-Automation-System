import yfinance as yf
import time
import os
from datetime import datetime

stocks = ["NVDA" , "AAPL" , "MSFT" , "GOOGL" , "AMZN" , "TSLA" , "META" , "AMD" , "INTC" , "NFLX" ,  ]

def monitor_stocks():
    """Monitor stock prices and display alerts"""
    for stock in stocks:
        ticker = yf.Ticker(stock)
        info = ticker.info
        Current_price = info['currentPrice']

        Previous_close = info['previousClose']

        change = Current_price - Previous_close
        percentage = (change / Previous_close) * 100

        if change > 0:
            symbol = "📈"
        else :
            symbol = "📉"
        print(f"Current price of {stock}: ${Current_price} {symbol}")
        print(f"Previous close of {stock}: ${Previous_close}")
        print(f"Change of {stock}: ${change:.2f} {symbol}")
        print(f"Percentage change of {stock}: {percentage:.2f}% {symbol}")
        print("-" * 40)  

        if abs(percentage) > 3.0:  
            print(f" BIG MOVE {stock} moved {percentage:.2f}%!")
            print(f" Current: ${Current_price} | Previous: ${Previous_close} | Change: ${change:.2f}")
            print(f"significant movement")


print(" Starting Stock Monitor with Auto-Refresh.")
print(" Press Ctrl+C to stop monitoring")
print("=" * 60)

try:
    while True:
        
        os.system('cls' if os.name == 'nt' else 'clear')
        
        
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"📈 STOCK MONITOR - Last Updated: {current_time}")
        print("=" * 60)
        
        
        monitor_stocks()


        print("\n Refreshing in 10 seconds , Ctrl+C to stop)")
        print("Monitoring 10 stocks for movements > 3%")
    
        time.sleep(10)
        
except KeyboardInterrupt:
    print("\n\nstopped.")
    