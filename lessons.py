# -*- coding: utf-8 -*-
"""
מודול השיעורים - כל השיעורים ללימוד Python
כל שיעור מכיל: הסבר, דוגמאות קוד, ותרגיל
"""

LESSONS = {
    1: {
        'title': '🎯 שיעור 1: מה זה Python ולמה הוא מגניב?',
        'content': """
היי! 👋 ברוכים הבאים לעולם המדהים של Python!

🐍 <b>מה זה Python?</b>
Python היא שפת תכנות שקל מאוד ללמוד ולהשתמש בה. היא כמו שפה שאתה מדבר עם המחשב, אבל במקום מילים סבוכות, Python משתמשת במילים פשוטות שאתה כבר מכיר!

💡 <b>למה Python היא כל כך מגניבה?</b>
• קל ללמוד - הקוד נראה כמעט כמו אנגלית רגילה
• עוצמתי - אפשר לעשות איתה כמעט הכל!
• פופולרי - חברות ענק כמו Google, Netflix ו-Instagram משתמשות ב-Python
• קהילה ענקית - מלא אנשים מוכנים לעזור

🎮 <b>מה אפשר לעשות עם Python?</b>
• לבנות אתרים
• לפתח בוטים (כמו הבוט הזה! 🤖)
• לעבוד עם בינוי מלאכותי
• לנתח מידע
• ליצור משחקים
• ועוד המון דברים מגניבים!

📝 <b>דוגמה ראשונה:</b>
<code>print("Hello World!")</code>

זה הקוד הראשון שכל מתכנת כותב! הפקודה print אומרת למחשב להציג משהו על המסך.

בשיעור הבא נלמד איך באמת לכתוב קוד Python!
""",
        'exercise': {
            'question': 'איזו מהחברות הבאות משתמשת ב-Python?',
            'options': ['Google', 'כולן', 'Netflix', 'Instagram'],
            'correct_answer': 'כולן',
            'explanation': 'נכון מאוד! כל החברות האלה משתמשות ב-Python למגוון פרויקטים! 🎉'
        }
    },
    
    2: {
        'title': '📝 שיעור 2: print - איך מציגים טקסט',
        'content': """
עכשיו בואו נלמד איך להדפיס טקסט על המסך! 🖨️

🎯 <b>הפקודה print</b>
זו אולי הפקודה הכי חשובה ב-Python! היא מאפשרת לנו להציג מידע למשתמש.

📌 <b>דוגמאות בסיסיות:</b>
<code>print("שלום עולם!")</code>
<code>print("אני לומד Python!")</code>
<code>print("זה ממש מגניב! 🚀")</code>

💬 <b>שימו לב!</b>
• הטקסט צריך להיות בתוך גרשיים: "..." או '...'
• שני הסוגים עובדים אותו דבר
• אפשר להדפיס גם אימוג׳ים! 😊

📊 <b>הדפסה של מספרים:</b>
<code>print(42)</code>
<code>print(3.14)</code>

מספרים לא צריכים גרשיים!

🎨 <b>כמה הדפסות ברצף:</b>
<code>print("שורה ראשונה")
print("שורה שנייה")
print("שורה שלישית")</code>

כל print יוצר שורה חדשה! ✨

🔥 <b>טריק מגניב - חיבור טקסטים:</b>
<code>print("שלום " + "עולם!")</code>
זה יציג: שלום עולם!

📚 <b>סיכום:</b>
• print מדפיס טקסט על המסך
• טקסט בגרשיים, מספרים בלי
• כל print יוצר שורה חדשה
""",
        'exercise': {
            'question': 'איזה קוד ידפיס "Python מגניב" בצורה נכונה?',
            'options': ['print(Python מגניב)', 'print Python מגניב', 'print("Python מגניב")', 'Print("Python מגניב")'],
            'correct_answer': 'print("Python מגניב")',
            'explanation': 'מצוין! 🎉 צריך גרשיים מסביב לטקסט, ו-print באותיות קטנות!'
        }
    },
    
    3: {
        'title': '📦 שיעור 3: משתנים - איך לשמור מידע',
        'content': """
בואו נלמד על משתנים - הדרך לשמור מידע בזיכרון! 💾

🎁 <b>מה זה משתנה?</b>
משתנה הוא כמו קופסה עם תווית שמאחסנת מידע. אתה יכול לשים בה מה שאתה רוצה ולהשתמש בזה מאוחר יותר!

📝 <b>איך יוצרים משתנה:</b>
<code>name = "אמיר"
age = 25
is_student = True</code>

זה פשוט! שם_המשתנה = ערך

🎯 <b>דוגמאות שימושיות:</b>
<code>city = "תל אביב"
temperature = 28
print(city)
print(temperature)</code>

עכשיו אפשר להשתמש במשתנים הללו כמה פעמים שרוצים!

🔄 <b>שינוי ערך משתנה:</b>
<code>score = 0
print(score)  # יציג: 0
score = 100
print(score)  # יציג: 100</code>

משתנים יכולים להשתנות! (זה בגלל זה הם נקראים משתנים 😄)

✨ <b>משתנים עם print:</b>
<code>name = "יוסי"
print("שלום " + name)  # יציג: שלום יוסי

age = 20
print("גיל:", age)  # יציג: גיל: 20</code>

📏 <b>כללי שמות למשתנים:</b>
✅ name, age, user_score
❌ 1name (לא להתחיל במספר)
❌ my-name (לא מקפים, רק קו תחתון)
✅ my_name (זה בסדר!)

🎨 <b>טיפ חשוב:</b>
תנו למשתנים שמות ברורים! במקום:
<code>x = "דני"</code>
עדיף:
<code>student_name = "דני"</code>

זה יעזור לכם (ולאחרים) להבין את הקוד!
""",
        'exercise': {
            'question': 'מה יודפס בקוד הזה?\n\nx = 5\nx = 10\nprint(x)',
            'options': ['5', '10', '5 10', 'שגיאה'],
            'correct_answer': '10',
            'explanation': 'נכון! 🌟 המשתנה x השתנה מ-5 ל-10, אז print מציג את הערך האחרון - 10'
        }
    },
    
    4: {
        'title': '🔢 שיעור 4: מספרים וחישובים מתמטיים',
        'content': """
בואו נהפוך את Python למחשבון מתקדם! 🧮

🔢 <b>סוגי מספרים ב-Python:</b>
• <b>מספרים שלמים (int):</b> 1, 42, -15, 1000
• <b>מספרים עשרוניים (float):</b> 3.14, -0.5, 2.0

📊 <b>פעולות חשבון בסיסיות:</b>
<code>print(5 + 3)    # חיבור: 8
print(10 - 4)   # חיסור: 6
print(6 * 7)    # כפל: 42
print(20 / 4)   # חילוק: 5.0
print(2 ** 3)   # חזקה: 8 (2³)</code>

💡 <b>שימו לב!</b>
החילוק (/) תמיד נותן מספר עשרוני, גם אם התוצאה שלמה!

🎯 <b>פעולות מתקדמות יותר:</b>
<code>print(17 // 5)  # חילוק שלם: 3 (בלי שארית)
print(17 % 5)   # שארית חילוק: 2</code>

הסימן % (מודולו) נותן את השארית של החילוק!

🧮 <b>משתנים וחישובים:</b>
<code>price = 100
discount = 20
final_price = price - discount
print(final_price)  # 80</code>

🔥 <b>קיצורי דרך נוחים:</b>
<code>score = 10
score = score + 5  # עכשיו score = 15

# דרך קצרה יותר:
score += 5   # אותו דבר! score = 20
score -= 3   # score = 17
score *= 2   # score = 34
score /= 2   # score = 17.0</code>

📐 <b>סדר פעולות חשבון:</b>
Python עובד כמו במתמטיקה! 
<code>result = 2 + 3 * 4
print(result)  # 14 (לא 20!)

# עם סוגריים:
result = (2 + 3) * 4
print(result)  # 20</code>

סדר הפעולות: סוגריים → חזקות → כפל/חילוק → חיבור/חיסור

🎨 <b>חישובים עם print:</b>
<code>print("5 + 3 =", 5 + 3)
print("תוצאה:", 10 * 2)</code>

💪 <b>דוגמה מעשית:</b>
<code>apples = 5
oranges = 3
total_fruits = apples + oranges
print("סך הכל פירות:", total_fruits)  # 8</code>
""",
        'exercise': {
            'question': 'מה התוצאה של: 10 + 5 * 2',
            'options': ['30', '20', '25', '15'],
            'correct_answer': '20',
            'explanation': 'מעולה! 🎯 כפל מתבצע לפני חיבור, אז: 5*2=10, ואז 10+10=20'
        }
    },
    
    5: {
        'title': '📝 שיעור 5: טקסטים (Strings) - עבודה עם מילים',
        'content': """
בואו נלמד איך לעבוד עם טקסט ב-Python! 🔤

📜 <b>מה זה String?</b>
String (מחרוזת) היא סדרה של תווים - מילים, משפטים, או כל טקסט!

✍️ <b>יצירת Strings:</b>
        <code>text1 = "שלום עולם"
        text2 = 'Python מגניב'
        text3 = \"\"\"טקסט
        בכמה
        שורות\"\"\"</code>

שני גרשיים רגילים או גרשיים משולשים לטקסט ארוך!

➕ <b>חיבור Strings:</b>
<code>first_name = "אמיר"
last_name = "חיים"
full_name = first_name + " " + last_name
print(full_name)  # אמיר חיים</code>

✖️ <b>שכפול Strings:</b>
<code>print("Ha" * 3)  # HaHaHa
print("🎉" * 5)  # 🎉🎉🎉🎉🎉</code>

כן, אפשר לכפול טקסט! 😄

📏 <b>אורך טקסט:</b>
<code>message = "Hello"
print(len(message))  # 5</code>

len מחזיר כמה תווים יש במחרוזת!

🔠 <b>אותיות גדולות וקטנות:</b>
<code>text = "python"
print(text.upper())  # PYTHON
print(text.lower())  # python
print(text.title())  # Python</code>

📍 <b>גישה לתווים ספציפיים:</b>
<code>word = "Python"
print(word[0])  # P (התו הראשון)
print(word[1])  # y (התו השני)
print(word[-1]) # n (התו האחרון)</code>

האינדקס מתחיל מ-0!

✂️ <b>חיתוך טקסט (Slicing):</b>
<code>text = "Hello World"
print(text[0:5])   # Hello
print(text[6:])    # World
print(text[:5])    # Hello</code>

🔍 <b>חיפוש בטקסט:</b>
<code>sentence = "אני אוהב Python"
print("Python" in sentence)  # True
print("Java" in sentence)    # False</code>

🎯 <b>החלפת טקסט:</b>
<code>text = "אני אוהב Java"
new_text = text.replace("Java", "Python")
print(new_text)  # אני אוהב Python</code>

🔢 <b>המרה למספרים ולהפך:</b>
<code># מטקסט למספר:
num = int("42")      # 42
decimal = float("3.14")  # 3.14

# ממספר לטקסט:
age = 25
text = str(age)      # "25"</code>

💫 <b>f-strings - דרך מודרנית לשלב משתנים:</b>
<code>name = "דני"
age = 20
print(f"שמי {name} ואני בן {age}")
# שמי דני ואני בן 20</code>

זו הדרך הכי נוחה! שימו ב-f לפני הגרשיים!
""",
        'exercise': {
            'question': 'מה יודפס?\n\ntext = "Python"\nprint(text[0] + text[-1])',
            'options': ['Pn', 'Py', 'Python', 'שגיאה'],
            'correct_answer': 'Pn',
            'explanation': 'מעולה! 🎊 text[0] הוא P (תו ראשון), text[-1] הוא n (תו אחרון), ביחד: Pn'
        }
    }
}

# המשך השיעורים יגיע בקובץ הבא...
