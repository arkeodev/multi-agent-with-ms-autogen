# filename: stock_news_debug.py
import requests

# Replace with your News API key
API_KEY = 'YOUR_API_KEY'
COMPANIES = ['NVIDIA', 'Tesla']

def fetch_news(company):
    url = f'https://newsapi.org/v2/everything?q={company}&sortBy=publishedAt&apiKey={API_KEY}'
    response = requests.get(url)
    print(f"Response for {company}: {response.json()}")  # Debug output
    return response.json()

for company in COMPANIES:
    news_data = fetch_news(company)
    print(f"Latest news for {company}:")
    if 'articles' in news_data and len(news_data['articles']) > 0:
        for article in news_data['articles'][:5]:  # Fetch top 5 articles
            print(f"- {article['title']} (Source: {article['source']['name']})")
    else:
        print("No articles found or an error occurred.")
    print("\n")