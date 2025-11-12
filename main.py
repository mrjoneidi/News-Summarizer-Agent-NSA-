# main.py
import schedule
import time
from config import Config
from rss_fetcher import fetch_news_from_rss
from summarizer import summarize
from storage import Storage
from notifier import send_summary
from utils import log

def job():
    log("شروع جمع‌آوری اخبار...")
    storage = Storage()
    seen = storage.load_seen()
    all_news = []

    for feed_url in Config.RSS_FEEDS:
        news = fetch_news_from_rss(feed_url, max_per_feed=Config.MAX_NEWS // len(Config.RSS_FEEDS) + 1)
        for item in news:
            title = item['title']
            if title in seen and seen[title] == item['pub_date']:
                continue  # تکراری

            full_text = f"{item['title']}\n{item['description']}"
            summary = summarize(full_text)

            processed = {
                'title': title,
                'summary': summary,
                'link': item['link'],
                'source': item['source']
            }
            all_news.append(processed)
            storage.save_news(title, item['pub_date'], summary, item['source'], item['link'])

            if len(all_news) >= Config.MAX_NEWS:
                break
        if len(all_news) >= Config.MAX_NEWS:
            break

    send_summary(all_news[:Config.MAX_NEWS])

# زمان‌بندی
schedule.every().day.at(Config.RUN_TIME).do(job)

# اولین اجرا
job()

log(f"Agent فعال شد. اجرا روزانه در ساعت {Config.RUN_TIME}")
while True:
    schedule.run_pending()
    time.sleep(60)