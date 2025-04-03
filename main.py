import instaloader
import os
import json
from telegram import Bot

# تنظیمات محیطی
TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
TELEGRAM_CHANNEL_ID = os.getenv("TELEGRAM_CHANNEL_ID")
INSTAGRAM_USERS = ["ft360_ir", "bbcpersian"]

bot = Bot(token=TELEGRAM_BOT_TOKEN)

# ⛔ بخش‌های مربوط به instaloader و session فعلاً حذف می‌شن
# چون فقط می‌خوایم تست کنیم که پیام به کانال می‌رسه یا نه

# ✅ ارسال یک پیام ساده به کانال برای تست
bot.send_message(chat_id=TELEGRAM_CHANNEL_ID, text="✅ تست موفق! ربات به تلگرام متصل است.", parse_mode="Markdown")
