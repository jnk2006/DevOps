# yfinance code goes here

### Basic yfinance example first
import yfinance as yf

def get_stock_info(ticker_symbol):
    # Fetch stock data
    stock = yf.Ticker(ticker_symbol)
    
    # Get stock info
    info = stock.info

    # Get current stock price
    current_price = stock.history(period="1d")['Close'][0]

    # Get past 30 days of stock prices
    past_30_days = stock.history(period="30d")['Close'].tolist()
    
    return info, current_price, past_30_days