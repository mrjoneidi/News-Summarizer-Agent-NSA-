# config.py
import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    TELEGRAM_TOKEN = os.getenv('TELEGRAM_TOKEN')
    TELEGRAM_CHAT_ID = os.getenv('TELEGRAM_CHAT_ID')
    LLM_API_KEY = os.getenv('LLM_API_KEY')
    LLM_BASE_URL = os.getenv('LLM_BASE_URL')
    RSS_FEEDS = [url.strip() for url in os.getenv('RSS_FEEDS', '').split(',') if url.strip()]
    MAX_NEWS = int(os.getenv('MAX_NEWS', 5))
    SUMMARY_LENGTH = int(os.getenv('SUMMARY_LENGTH', 100))
    RUN_TIME = os.getenv('RUN_TIME', '08:00') 
    CSV_FILE = 'news_history.csv'