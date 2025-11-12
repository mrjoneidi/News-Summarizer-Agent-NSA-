# storage.py
import pandas as pd
import os
from config import Config
from utils import log
from datetime import datetime

class Storage:
    def __init__(self, file_path=Config.CSV_FILE):
        self.file_path = file_path

    def load_seen(self):
        """برمی‌گرداند: {title: pub_date}"""
        if not os.path.exists(self.file_path):
            return {}
        try:
            df = pd.read_csv(self.file_path)
            return dict(zip(df['title'], df['pub_date']))
        except Exception as e:
            log(f"خطا در خواندن تاریخچه: {e}", "error")
            return {}

    def save_news(self, title, pub_date, summary, source, link):
        df = pd.DataFrame([{
            'title': title,
            'pub_date': pub_date,
            'summary': summary,
            'source': source,
            'link': link,
            'date_added': datetime.now().isoformat()
        }])
        header = not os.path.exists(self.file_path)
        df.to_csv(self.file_path, mode='a', header=header, index=False)
        log(f"News Saved {title}")