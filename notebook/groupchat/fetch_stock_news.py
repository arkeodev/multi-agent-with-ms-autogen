# filename: fetch_stock_news.py
import requests
from bs4 import BeautifulSoup

def fetch_news(ticker):
    url = f"https://finance.yahoo.com/quote/{ticker}/news?p={ticker}"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    headlines = []
    for item in soup.find_all('h3', class_='Mb(5px)'):
        link = item.find('a')
        headline = link.get_text() if link else item.get_text()
        headlines.append(headline.strip())
        
    return headlines[:5]  # Get the top 5 news headlines

nvidia_news = fetch_news("NVDA")
tesla_news = fetch_news("TSLA")

print("NVIDIA Recent News Headlines:")
for news in nvidia_news:
    print("-", news)

print("\nTesla Recent News Headlines:")
for news in tesla_news:
    print("-", news)