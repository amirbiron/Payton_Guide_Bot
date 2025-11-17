#!/bin/bash

# סקריפט התקנה מהיר לבוט לימוד פייתון

echo "🎓 התקנת בוט לימוד פייתון..."
echo ""

# בדיקת Python
echo "🔍 בודק התקנת Python..."
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 לא מותקן!"
    echo "התקן Python מ: https://www.python.org/downloads/"
    exit 1
fi

echo "✅ Python מותקן: $(python3 --version)"
echo ""

# בדיקת pip
echo "🔍 בודק pip..."
if ! command -v pip3 &> /dev/null; then
    echo "❌ pip לא מותקן!"
    exit 1
fi

echo "✅ pip מותקן"
echo ""

# התקנת תלויות
echo "📦 מתקין תלויות..."
pip3 install -r requirements.txt

echo ""
echo "✅ ההתקנה הושלמה בהצלחה!"
echo ""
echo "📝 צעדים הבאים:"
echo "1. פתח את bot.py"
echo "2. שים את הטוקן של הבוט בשורה 8:"
echo "   BOT_TOKEN = \"YOUR_BOT_TOKEN_HERE\""
echo ""
echo "3. הרץ את הבוט:"
echo "   python3 bot.py"
echo ""
echo "💡 איך לקבל טוקן?"
echo "   1. פתח @BotFather בטלגרם"
echo "   2. שלח /newbot"
echo "   3. עקוב אחרי ההוראות"
echo ""
echo "🚀 בהצלחה!"
