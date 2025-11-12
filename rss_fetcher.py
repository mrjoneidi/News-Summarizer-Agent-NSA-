# rss_fetcher.py
import feedparser
from utils import log

def fetch_news_from_rss(feed_url, max_per_feed=3):
    try:
        feed = feedparser.parse(feed_url)
        source = feed.feed.get('title', feed_url)
        entries = feed.entries[:max_per_feed]
        news = []
        for entry in entries:
            news.append({
                'title': entry.title,
                'link': entry.link,
                'pub_date': entry.get('published', ''),
                'description': entry.get('summary', entry.get('description', '')),
                'source': source
            })
        log(f"{len(entries)} خبر از {source} دریافت شد.")
        return news
    except Exception as e:
        log(f"خطا در RSS {feed_url}: {e}", "error")
        return []