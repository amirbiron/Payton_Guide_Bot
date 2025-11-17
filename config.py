import os
from dotenv import load_dotenv

# טעינת משתני סביבה
load_dotenv()

# הגדרות Telegram
TELEGRAM_BOT_TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')

# הגדרות MongoDB
MONGODB_URI = os.getenv('MONGODB_URI')
DB_NAME = os.getenv('DB_NAME', 'python_learning_bot')

# בדיקת תקינות
if not TELEGRAM_BOT_TOKEN:
    raise ValueError("TELEGRAM_BOT_TOKEN לא הוגדר!")

if not MONGODB_URI:
    raise ValueError("MONGODB_URI לא הוגדר!")
