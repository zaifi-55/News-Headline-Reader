# News Headline Reader

A simple Python app that fetches top headlines using NewsAPI and reads them aloud using pyttsx3.

## Features
- Choose news category and country
- Fetches live headlines from NewsAPI
- Text-to-speech (offline) reading

## Setup
1. Clone repo
2. Create virtualenv: `python -m venv venv` and activate it
3. Install deps: `pip install -r requirements.txt` (or `pip install requests python-dotenv pyttsx3`)
4. Add `.env` file with `NEWSAPI_KEY=your_key_here`
5. Run `python news_reader.py`

