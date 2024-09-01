# filename: stock_prices.py
import requests
import datetime

def get_stock_data(symbol):
    # URL for the Alpha Vantage API
    API_KEY = 'YOUR_API_KEY'  # Replace with your Alpha Vantage API key
    url = f'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={symbol}&apikey={API_KEY}'
    
    response = requests.get(url)
    data = response.json()
    
    # Output the raw data to help troubleshoot
    print(f"Raw data for {symbol}: {data}")

    # Check if the data is valid
    if 'Time Series (Daily)' not in data:
        return None, None

    # Get today's date
    today = datetime.date.today()
    
    # Fetch today's price
    today_str = today.strftime('%Y-%m-%d')
    try:
        today_price = float(data['Time Series (Daily)'][today_str]['4. close'])
    except KeyError:
        today_price = None
    
    # Get price one month ago
    one_month_ago = today - datetime.timedelta(days=30)
    one_month_ago_str = one_month_ago.strftime('%Y-%m-%d')
    
    try:
        one_month_ago_price = float(data['Time Series (Daily)'][one_month_ago_str]['4. close'])
    except KeyError:
        one_month_ago_price = None

    return today_price, one_month_ago_price

nvda_current, nvda_past = get_stock_data('NVDA')
tsla_current, tsla_past = get_stock_data('TSLA')