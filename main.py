import instaloader
import os
import datetime
from telegram import Bot

# تنظیمات
TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
TELEGRAM_CHANNEL_ID = os.getenv("TELEGRAM_CHANNEL_ID")

bot = Bot(token=TELEGRAM_BOT_TOKEN)

# بارگذاری session اینستاگرام
loader = instaloader.Instaloader()
loader.load_session_from_file("moshaveranpooya", filename="session-moshaveranpooya")

try:
    profile = instaloader.Profile.from_username(loader.context, "ft360_ir")
    posts = profile.get_posts()

    now = datetime.datetime.now()
    cutoff_time = now - datetime.timedelta(hours=24)

    sent_any = False
    for i, post in enumerate(posts):
        if i >= 5:
            break  # فقط ۵ پست آخر رو بررسی کن

        post_time = post.date_local

        if post_time > cutoff_time:
            post_url = f"https://www.instagram.com/p/{post.shortcode}/"
            caption = post.caption or ""
            message = f"{caption}\n\n📌 [مشاهده پست در اینستاگرام]({post_url})"

            bot.send_photo(
                chat_id=TELEGRAM_CHANNEL_ID,
                photo=post.url,
                caption=message,
                parse_mode="Markdown"
            )
            print(f"✅ پست ارسال شد: {post.shortcode}")
            sent_any = True
        else:
            print(f"⏳ پست {post.shortcode} قدیمیه ({post_time}), ارسال نمی‌شه.")

    if not sent_any:
        print("ℹ️ هیچ پست جدیدی در ۲۴ ساعت گذشته نبود.")

except Exception as e:
    print(f"❌ خطا در دریافت یا ارسال پست: {e}")
