from dotenv import load_dotenv
import os
import requests
import pyttsx3

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
    resp=requests.get(url,params=params)
    resp.raise_for_status()
    data=resp.json()
    if data.get("status") !="ok":
        raise Exception("API error: " +str(data))
    return[a.get("title") for a in data.get("articles",[])]

def speak_headlines(headlines):
    engine=pyttsx3.init()
    engine.setProperty('rate',150)
    for idx,title in enumerate(headlines,start=1):
        text=f"Headline {idx}:{title}"
        print(text)
        engine.say(text)
    engine.runAndWait()


if __name__ == "__main__":
    cat=input("Enter category (technology,business,sports,health,entertainment) [default: technology]: ") or "technology"
    country=input("Enter country code (us,gb,in) [default: us]: ") or "us"
    headlines=get_headlines(category=cat,country=country,page_size=5)
    speak_headlines(headlines)
