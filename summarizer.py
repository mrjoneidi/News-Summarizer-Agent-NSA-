# summarizer.py
import openai
from config import Config
from utils import log

client = openai.OpenAI(
    api_key=Config.LLM_API_KEY,
    base_url= Config.LLM_BASE_URL
)

def summarize(text):
    try:
        response = client.chat.completions.create(
            model="grok-beta",
            messages=[
                {"role": "system", "content": "خلاصه فارسی، کوتاه، دقیق و بدون偏اس بنویس. حداکثر ۱۰۰ کلمه."},
                {"role": "user", "content": text}
            ],
            max_tokens=Config.SUMMARY_LENGTH,
            temperature=0.5
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        log(f"خطا در خلاصه‌سازی: {e}", "error")
        return text[:200] + "..."  