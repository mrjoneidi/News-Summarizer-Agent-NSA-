# notifier.py
from telegram import Bot
from config import Config
from utils import log
import asyncio

bot = Bot(token=Config.TELEGRAM_TOKEN)

async def send_summary_async(news_list):
    if not news_list:
        return

    message = "خلاصه اخبار امروز\n\n"
    for item in news_list:
        message += f"*{item['title']}*\n"
        message += f"{item['summary']}\n"
        message += f"منبع: {item['source']}\n"
        message += f"[بخوانید]({item['link']})\n\n"

    try:
        await bot.send_message(
            chat_id=Config.TELEGRAM_CHAT_ID,
            text=message,
            parse_mode='Markdown',
            disable_web_page_preview=True
        )
        log(f"{len(news_list)} خبر ارسال شد.")
    except Exception as e:
        log(f"خطا در ارسال تلگرام: {e}", "error")

def send_summary(news_list):
    asyncio.run(send_summary_async(news_list))