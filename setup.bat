@echo off
REM סקריפט התקנה מהיר לבוט לימוד פייתון (Windows)

echo 🎓 התקנת בוט לימוד פייתון...
echo.

REM בדיקת Python
echo 🔍 בודק התקנת Python...
python --version >nul 2>&1
if errorlevel 1 (
    echo ❌ Python לא מותקן!
    echo התקן Python מ: https://www.python.org/downloads/
    pause
    exit /b 1
)

echo ✅ Python מותקן
python --version
echo.

REM התקנת תלויות
echo 📦 מתקין תלויות...
pip install -r requirements.txt

echo.
echo ✅ ההתקנה הושלמה בהצלחה!
echo.
echo 📝 צעדים הבאים:
echo 1. פתח את bot.py
echo 2. שים את הטוקן של הבוט בשורה 8:
echo    BOT_TOKEN = "YOUR_BOT_TOKEN_HERE"
echo.
echo 3. הרץ את הבוט:
echo    python bot.py
echo.
echo 💡 איך לקבל טוקן?
echo    1. פתח @BotFather בטלגרם
echo    2. שלח /newbot
echo    3. עקוב אחרי ההוראות
echo.
echo 🚀 בהצלחה!
echo.
pause
