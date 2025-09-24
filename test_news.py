import requests
import os
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

NEWS_API_KEY = os.getenv("e9ba34a7a84b452b9605434f8c8d9782")

if not NEWS_API_KEY:
    print("❌ NEWS_API_KEY not found in .env file")
else:
    url = f"https://newsapi.org/v2/top-headlines?country=us&apiKey={e9ba34a7a84b452b9605434f8c8d9782}"

    res = requests.get(url)
    data = res.json()

    if data.get("status") != "ok":
        print("❌ Error fetching news:", data.get("message", "Unknown error"))
    else:
        articles = data.get("articles", [])
        if not articles:
            print("⚠️ No news articles found.")
        else:
            print("📰 Top Headlines:\n")
            for i, article in enumerate(articles[:5], start=1):  # show first 5
                print(f"{i}. {article['title']}")
                print(f"   Source: {article['source']['name']}")
                print(f"   Link: {article['url']}\n")
