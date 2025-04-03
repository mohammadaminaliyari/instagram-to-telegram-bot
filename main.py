import instaloader
import os
from telegram import Bot

# تنظیمات
TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
TELEGRAM_CHANNEL_ID = os.getenv("TELEGRAM_CHANNEL_ID")

bot = Bot(token=TELEGRAM_BOT_TOKEN)

# اتصال به اینستاگرام با session
loader = instaloader.Instaloader()
loader.load_session_from_file("moshaveranpooya", filename="session-moshaveranpooya")

try:
    profile = instaloader.Profile.from_username(loader.context, "ft360_ir")
    latest_post = next(profile.get_posts())  # گرفتن آخرین پست

    post_url = f"https://www.instagram.com/p/{latest_post.shortcode}/"
    caption = latest_post.caption or ""
    message = f"{caption}\n\n📌 [مشاهده پست در اینستاگرام]({post_url})"

    # ارسال پست به تلگرام
    bot.send_photo(
        chat_id=TELEGRAM_CHANNEL_ID,
        photo=latest_post.url,
        caption=message,
        parse_mode="Markdown"
    )

    print("✅ پست آخر ft360_ir با موفقیت ارسال شد!")

except Exception as e:
    print(f"❌ خطا در دریافت یا ارسال پست: {e}")
