# filename: stock_prices_yahoo.py
import yfinance as yf
import datetime

def get_stock_data(symbol):
    stock = yf.Ticker(symbol)
    today = datetime.date.today()
    one_month_ago = today - datetime.timedelta(days=30)

    # Get the historical data for the past month
    hist = stock.history(start=one_month_ago, end=today)

    if hist.empty:
        return None, None

    today_price = hist['Close'][-1]
    one_month_ago_price = hist['Close'][0]

    return today_price, one_month_ago_price

def calculate_percentage_change(current_price, past_price):
    if past_price is None or current_price is None:
        return None
    return ((current_price - past_price) / past_price) * 100

nvda_current, nvda_past = get_stock_data('NVDA')
tsla_current, tsla_past = get_stock_data('TSLA')

# Prepare output with error handling
nvda_change = calculate_percentage_change(nvda_current, nvda_past)
tsla_change = calculate_percentage_change(tsla_current, tsla_past)

nvda_output = f"NVIDIA (NVDA) Current Price: ${nvda_current:.2f}" if nvda_current is not None else "NVIDIA (NVDA) data not available"
nvda_output += f", 1-Month Change: {nvda_change:.2f}%" if nvda_change is not None else ", 1-Month Change: data not available"

tsla_output = f"Tesla (TSLA) Current Price: ${tsla_current:.2f}" if tsla_current is not None else "Tesla (TSLA) data not available"
tsla_output += f", 1-Month Change: {tsla_change:.2f}%" if tsla_change is not None else ", 1-Month Change: data not available"

print(nvda_output)
print(tsla_output)