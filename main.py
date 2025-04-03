import instaloader
import os
import json
from telegram import Bot

# تنظیمات محیطی
TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
TELEGRAM_CHANNEL_ID = os.getenv("TELEGRAM_CHANNEL_ID")
INSTAGRAM_SESSION_USER = os.getenv("INSTAGRAM_SESSION_USER")
INSTAGRAM_USERS = ["ft360_ir", "bbcpersian"]
SENT_POSTS_FILE = "sent_posts.json"

bot = Bot(token=TELEGRAM_BOT_TOKEN)

# فایل لیست پست‌های ارسال‌شده
if os.path.exists(SENT_POSTS_FILE):
    with open(SENT_POSTS_FILE, "r") as f:
        sent_posts = json.load(f)
else:
    sent_posts = []

# لاگین به اینستاگرام با session
loader = instaloader.Instaloader()
loader.load_session_from_file("moshaveranpooya")

for username in INSTAGRAM_USERS:
    try:
        profile = instaloader.Profile.from_username(loader.context, username)
        posts = profile.get_posts()
        for post in posts:
            shortcode = post.shortcode
            if shortcode in sent_posts:
                continue
            post_url = f"https://www.instagram.com/p/{shortcode}/"
            caption = post.caption or ""
            message = f"{caption}\n\n📌 [مشاهده پست در اینستاگرام]({post_url})"

            bot.send_photo(chat_id=TELEGRAM_CHANNEL_ID, photo=post.url, caption=message, parse_mode="Markdown")

            sent_posts.append(shortcode)
            break  # فقط یک پست جدید از هر پیج

    except Exception as e:
        print(f"خطا در دریافت پست از {username}: {e}")

with open(SENT_POSTS_FILE, "w") as f:
    json.dump(sent_posts, f)
