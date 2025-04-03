import instaloader
import os
from telegram import Bot
import datetime

# تنظیمات توکن (فقط لازمه که ساختار ثابت بمونه)
TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
TELEGRAM_CHANNEL_ID = os.getenv("TELEGRAM_CHANNEL_ID")

# بارگذاری session
loader = instaloader.Instaloader()
loader.load_session_from_file("moshaveranpooya", filename="session-moshaveranpooya")

try:
    profile = instaloader.Profile.from_username(loader.context, "ft360_ir")
    latest_post = next(profile.get_posts())

    # اطلاعات کامل پست
    print("🔍 Debug اطلاعات آخرین پست:\n")
    print(f"🆔 Shortcode: {latest_post.shortcode}")
    print(f"📅 تاریخ انتشار (Local): {latest_post.date_local}")
    print(f"📅 تاریخ انتشار (UTC): {latest_post.date_utc}")
    print(f"📎 نوع محتوا: {'ویدیو' if latest_post.is_video else 'عکس'}")
    print(f"📸 URL: {latest_post.url}")
    print(f"📝 کپشن:\n{latest_post.caption}")
    print("\n✅ بررسی پست کامل شد.")

except Exception as e:
    print(f"❌ خطا در دریافت پست: {e}")
