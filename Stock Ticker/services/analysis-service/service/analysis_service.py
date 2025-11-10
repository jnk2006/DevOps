import yfinance as yf
import pandas as pd

def calculate_moving_averages(ticker, period='3mo'):
    """Calculate 7-day and 30-day moving averages"""
    try:
        stock = yf.Ticker(ticker)
        hist = stock.history(period=period)
        
        if hist.empty:
            raise ValueError(f"No data found for {ticker}")
        
        # Calculate moving averages
        hist['MA7'] = hist['Close'].rolling(window=7).mean()
        hist['MA30'] = hist['Close'].rolling(window=30).mean()
        
        # Get latest values
        latest = hist.iloc[-1]
        
        result = {
            'ma_7': float(latest['MA7']) if not pd.isna(latest['MA7']) else None,
            'ma_30': float(latest['MA30']) if not pd.isna(latest['MA30']) else None,
            'signal': get_signal(latest['Close'], latest['MA7'], latest['MA30'])
        }
        
        return result
    except Exception as e:
        raise Exception(f"Analysis error: {str(e)}")

def get_signal(price, ma7, ma30):
    """Generate buy/sell/hold signal"""
    if pd.isna(ma7) or pd.isna(ma30):
        return "INSUFFICIENT_DATA"
    
    if price > ma7 and ma7 > ma30:
        return "BUY"
    elif price < ma7 and ma7 < ma30:
        return "SELL"
    else:
        return "HOLD"