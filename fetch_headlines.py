from dotenv import load_dotenv
import os
import requests

load_dotenv()
API_KEY=os.getenv("NEWSAPI_KEY")

def get_headlines(category="technology",country="us",page_size=5):
    url="https://newsapi.org/v2/top-headlines"
    params={
        "country":country,
        "category":category,
        "pageSize":page_size,
        "apiKey":API_KEY
    }
    resp=requests.get(url, params=params)
    resp.raise_for_status()
    data=resp.json()
    if data.get("status") !="ok":
        raise Exception("API returned an error: " +str(data))

    return [article.get("title") for article in data.get("articles",[])]


if __name__ == "__main__":
    headlines=get_headlines(category="technology",country="us",page_size=5)
    for idx,title in enumerate(headlines,start=1):
        print(f"{idx}.{title}")


