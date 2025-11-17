import os
import json
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, MessageHandler, filters, ContextTypes

# טוכן הבוט שלך (תשים את זה ב-environment variable או כאן)
BOT_TOKEN = "YOUR_BOT_TOKEN_HERE"

# נתיב לשמירת התקדמות משתמשים
USER_DATA_FILE = "user_progress.json"

# ====================
# תוכן השיעורים - 20 שיעורים מלאים!
# ====================
LESSONS = {
    1: {
        "title": "🎯 מהו פייתון?",
        "content": """
<b>ברוכים הבאים לשיעור הראשון! 🎉</b>

<b>מהו פייתון?</b>
פייתון היא שפת תכנות פשוטה וחזקה שמשמשת למיליוני מפתחים ברחבי העולם.

<b>למה פייתון?</b>
✅ קלה ללמידה - תחביר פשוט וברור
✅ רבת עוצמה - אפשר לבנות כמעט הכל
✅ מבוקשת בשוק העבודה
✅ קהילה ענקית ותומכת

<b>דוגמה לקוד פייתון הראשון שלך:</b>
<code>print("Hello, World!")</code>

זה הכל! שורה אחת שמדפיסה טקסט למסך 😊
        """,
        "exercise": {
            "question": "מה הפקודה שמדפיסה טקסט למסך?",
            "answer": "print",
            "hint": "רמז: זה באנגלית ופירושו 'להדפיס'"
        }
    },
    2: {
        "title": "📦 משתנים - איך לשמור מידע",
        "content": """
<b>שיעור 2: משתנים 📦</b>

<b>מהו משתנה?</b>
משתנה הוא כמו קופסה שבה אנחנו שומרים מידע.

<b>איך יוצרים משתנה?</b>
<code>name = "דני"
age = 25
height = 1.75</code>

<b>כללים חשובים:</b>
✅ שם המשתנה באנגלית (לרוב)
✅ לא מתחיל במספר
✅ אפשר להשתמש ב-_ (קו תחתון)
✅ רגיש לאותיות גדולות/קטנות

<b>דוגמה:</b>
<code>favorite_color = "כחול"
print(favorite_color)  # מדפיס: כחול</code>
        """,
        "exercise": {
            "question": "איך נכתוב משתנה ששומר את המספר 100?",
            "answer": "number = 100",
            "hint": "רמז: [שם_משתנה] = [ערך]"
        }
    },
    3: {
        "title": "🔢 סוגי נתונים - מספרים וטקסט",
        "content": """
<b>שיעור 3: סוגי נתונים 🔢</b>

בפייתון יש כמה סוגי נתונים עיקריים:

<b>1. מספרים שלמים (int):</b>
<code>age = 25
score = 100</code>

<b>2. מספרים עשרוניים (float):</b>
<code>height = 1.75
price = 19.99</code>

<b>3. טקסט (string/str):</b>
<code>name = "דני"
message = 'שלום עולם'</code>

<b>4. בוליאני - אמת/שקר (bool):</b>
<code>is_student = True
is_ready = False</code>

<b>איך לבדוק סוג נתון?</b>
<code>type(25)  # תוצאה: int
type("שלום")  # תוצאה: str</code>
        """,
        "exercise": {
            "question": "מה סוג הנתון של המספר 3.14?",
            "answer": "float",
            "hint": "רמז: זה מספר עשרוני..."
        }
    },
    4: {
        "title": "➕ פעולות מתמטיות",
        "content": """
<b>שיעור 4: חשבון בפייתון ➕➖✖️➗</b>

פייתון יכולה לשמש כמחשבון מתקדם!

<b>פעולות בסיסיות:</b>
<code>10 + 5   # חיבור = 15
10 - 5   # חיסור = 5
10 * 5   # כפל = 50
10 / 5   # חילוק = 2.0
10 // 3  # חילוק שלם = 3
10 % 3   # שארית = 1
2 ** 3   # חזקה (2³) = 8</code>

<b>שימוש עם משתנים:</b>
<code>price = 100
discount = 20
final_price = price - discount
print(final_price)  # 80</code>

<b>טיפ מקצועי:</b>
אפשר לשלב פעולות: <code>result = (10 + 5) * 2</code>
        """,
        "exercise": {
            "question": "מה התוצאה של 10 // 3 (חילוק שלם)?",
            "answer": "3",
            "hint": "רמז: חילוק שלם מתעלם מהשארית"
        }
    },
    5: {
        "title": "💬 קלט ופלט - שיחה עם המשתמש",
        "content": """
<b>שיעור 5: קלט ופלט 💬</b>

איך התוכנית שלנו מדברת עם המשתמש?

<b>1. פלט - להדפיס מידע (print):</b>
<code>print("שלום!")
print("הגיל שלי:", 25)</code>

<b>2. קלט - לקבל מידע (input):</b>
<code>name = input("מה שמך? ")
print("שלום", name)</code>

<b>דוגמה מלאה:</b>
<code>name = input("מה שמך? ")
age = input("בן כמה אתה? ")
print(f"שלום {name}, נחמד להכיר!")</code>

<b>⚠️ חשוב!</b>
input תמיד מחזיר טקסט (string).
אם צריך מספר, צריך להמיר:
<code>age = int(input("בן כמה? "))</code>
        """,
        "exercise": {
            "question": "איזו פונקציה מקבלת קלט מהמשתמש?",
            "answer": "input",
            "hint": "רמז: באנגלית פירושו 'קלט'"
        }
    },
    6: {
        "title": "🔄 לולאות - חזרה על פעולות",
        "content": """
<b>שיעור 6: לולאות 🔄</b>

לולאה היא דרך לחזור על פעולה כמה פעמים.

<b>לולאת for - חזרה מספר ידוע של פעמים:</b>
<code>for i in range(5):
    print(i)  # ידפיס: 0, 1, 2, 3, 4</code>

<b>חזרה על רשימה:</b>
<code>fruits = ["תפוח", "בננה", "תפוז"]
for fruit in fruits:
    print(fruit)</code>

<b>לולאת while - חזרה עד שתנאי מתקיים:</b>
<code>count = 0
while count < 5:
    print(count)
    count += 1</code>

<b>⚠️ טיפ חשוב:</b>
תמיד וודא שהלולאה תיעצר! אחרת זו לולאה אינסופית.
        """,
        "exercise": {
            "question": "איזו מילת מפתח משמשת להתחלת לולאה?",
            "answer": "for",
            "hint": "רמז: באנגלית פירושו 'עבור'"
        }
    },
    7: {
        "title": "🔀 תנאים - קבלת החלטות",
        "content": """
<b>שיעור 7: משפטי תנאי 🔀</b>

תנאים מאפשרים לתוכנית לקבל החלטות!

<b>תנאי בסיסי (if):</b>
<code>age = 18
if age >= 18:
    print("אתה בוגר!")</code>

<b>if-else:</b>
<code>if age >= 18:
    print("אתה בוגר")
else:
    print("אתה קטין")</code>

<b>if-elif-else:</b>
<code>grade = 85
if grade >= 90:
    print("מעולה!")
elif grade >= 80:
    print("טוב מאוד")
elif grade >= 70:
    print("טוב")
else:
    print("צריך לשפר")</code>

<b>אופרטורי השוואה:</b>
<code>==  # שווה
!=  # לא שווה
>   # גדול מ
<   # קטן מ
>=  # גדול או שווה
<=  # קטן או שווה</code>
        """,
        "exercise": {
            "question": "איזו מילת מפתח מתחילה תנאי?",
            "answer": "if",
            "hint": "רמז: באנגלית זה 'אם'"
        }
    },
    8: {
        "title": "📋 רשימות - אוספי נתונים",
        "content": """
<b>שיעור 8: רשימות (Lists) 📋</b>

רשימה היא אוסף של פריטים ממוספרים.

<b>יצירת רשימה:</b>
<code>fruits = ["תפוח", "בננה", "תפוז"]
numbers = [1, 2, 3, 4, 5]
mixed = [1, "שלום", 3.14, True]</code>

<b>גישה לפריטים:</b>
<code>print(fruits[0])  # תפוח (אינדקס מתחיל מ-0!)
print(fruits[1])  # בננה
print(fruits[-1])  # תפוז (האחרון)</code>

<b>פעולות על רשימות:</b>
<code>fruits.append("אבטיח")  # הוסף בסוף
fruits.remove("בננה")  # הסר פריט
len(fruits)  # אורך הרשימה
fruits[0] = "אגס"  # שנה פריט</code>

<b>חיתוך רשימות (slicing):</b>
<code>numbers = [0, 1, 2, 3, 4, 5]
print(numbers[1:4])  # [1, 2, 3]
print(numbers[:3])   # [0, 1, 2]
print(numbers[3:])   # [3, 4, 5]</code>
        """,
        "exercise": {
            "question": "מה האינדקס של הפריט הראשון ברשימה?",
            "answer": "0",
            "hint": "רמז: בפייתון האינדקס מתחיל מאפס!"
        }
    },
    9: {
        "title": "⚙️ פונקציות - קוד לשימוש חוזר",
        "content": """
<b>שיעור 9: פונקציות ⚙️</b>

פונקציה היא בלוק קוד שאפשר להריץ מתי שרוצים!

<b>הגדרת פונקציה:</b>
<code>def say_hello():
    print("שלום!")

say_hello()  # קריאה לפונקציה</code>

<b>פונקציה עם פרמטרים:</b>
<code>def greet(name):
    print(f"שלום {name}!")

greet("דני")  # שלום דני!</code>

<b>פונקציה שמחזירה ערך:</b>
<code>def add(a, b):
    return a + b

result = add(5, 3)  # result = 8</code>

<b>פרמטרים עם ברירת מחדל:</b>
<code>def power(base, exp=2):
    return base ** exp

print(power(3))     # 9 (3²)
print(power(3, 3))  # 27 (3³)</code>

<b>למה פונקציות?</b>
✅ קוד מסודר וקריא
✅ שימוש חוזר
✅ קל לתחזוקה
        """,
        "exercise": {
            "question": "איזו מילת מפתח מגדירה פונקציה?",
            "answer": "def",
            "hint": "רמז: קיצור של 'define'"
        }
    },
    10: {
        "title": "📖 מילונים - מיפוי מפתח-ערך",
        "content": """
<b>שיעור 10: מילונים (Dictionaries) 📖</b>

מילון הוא אוסף של זוגות מפתח-ערך.

<b>יצירת מילון:</b>
<code>person = {
    "name": "דני",
    "age": 25,
    "city": "תל אביב"
}</code>

<b>גישה לערכים:</b>
<code>print(person["name"])  # דני
print(person.get("age"))  # 25</code>

<b>שינוי והוספה:</b>
<code>person["age"] = 26  # שינוי
person["job"] = "מתכנת"  # הוספה</code>

<b>מחיקה:</b>
<code>del person["city"]  # מחק מפתח</code>

<b>לולאה על מילון:</b>
<code># רק מפתחות
for key in person:
    print(key)

# מפתחות וערכים
for key, value in person.items():
    print(f"{key}: {value}")</code>

<b>בדיקת קיום מפתח:</b>
<code>if "name" in person:
    print("קיים!")</code>
        """,
        "exercise": {
            "question": "איזה סימן משמש לגישה לערך במילון?",
            "answer": "[]",
            "hint": "רמז: סוגריים מרובעים..."
        }
    },
    11: {
        "title": "🎭 טאפלים וסטים",
        "content": """
<b>שיעור 11: טאפלים וסטים 🎭</b>

<b>טאפל (Tuple) - רשימה שלא משתנה:</b>
<code>coordinates = (10, 20)
rgb = (255, 128, 0)

# אי אפשר לשנות!
# coordinates[0] = 15  # שגיאה!</code>

<b>מתי להשתמש בטאפל?</b>
✅ כשהנתונים לא אמורים להשתנות
✅ מהיר יותר מרשימה
✅ יכול לשמש כמפתח במילון

<b>סט (Set) - אוסף ללא כפילויות:</b>
<code>numbers = {1, 2, 3, 4, 5}
numbers.add(3)  # לא יוסיף - כבר קיים
print(numbers)  # {1, 2, 3, 4, 5}</code>

<b>פעולות על סטים:</b>
<code>a = {1, 2, 3}
b = {3, 4, 5}

print(a | b)  # איחוד: {1, 2, 3, 4, 5}
print(a & b)  # חיתוך: {3}
print(a - b)  # הפרש: {1, 2}</code>
        """,
        "exercise": {
            "question": "איזה מבנה נתונים לא ניתן לשינוי?",
            "answer": "tuple",
            "hint": "רמז: טאפל או tuple"
        }
    },
    12: {
        "title": "🔤 מחרוזות - עבודה עם טקסט",
        "content": """
<b>שיעור 12: מחרוזות מתקדמות 🔤</b>

<b>פעולות בסיסיות:</b>
<code>text = "שלום עולם"
print(len(text))  # אורך
print(text.upper())  # אותיות גדולות
print(text.lower())  # אותיות קטנות</code>

<b>חיתוך מחרוזות:</b>
<code>text = "Python"
print(text[0])    # P
print(text[-1])   # n
print(text[0:3])  # Pyt</code>

<b>חיפוש והחלפה:</b>
<code>text = "I love Python"
print("Python" in text)  # True
print(text.replace("love", "like"))</code>

<b>פיצול וחיבור:</b>
<code>sentence = "אני אוהב לתכנת"
words = sentence.split()  # ['אני', 'אוהב', 'לתכנת']
joined = " ".join(words)  # חזרה למשפט</code>

<b>f-strings - עיצוב מתקדם:</b>
<code>name = "דני"
age = 25
print(f"{name} בן {age}")  # דני בן 25</code>
        """,
        "exercise": {
            "question": "איזו פונקציה מחזירה את אורך מחרוזת?",
            "answer": "len",
            "hint": "רמז: קיצור של length"
        }
    },
    13: {
        "title": "📁 עבודה עם קבצים",
        "content": """
<b>שיעור 13: קריאה וכתיבה לקבצים 📁</b>

<b>כתיבה לקובץ:</b>
<code>file = open("message.txt", "w")
file.write("שלום עולם!")
file.close()</code>

<b>קריאה מקובץ:</b>
<code>file = open("message.txt", "r")
content = file.read()
print(content)
file.close()</code>

<b>דרך טובה יותר - with:</b>
<code>with open("message.txt", "w") as file:
    file.write("שלום!")
# הקובץ נסגר אוטומטית!</code>

<b>קריאה שורה שורה:</b>
<code>with open("data.txt", "r") as file:
    for line in file:
        print(line.strip())</code>

<b>מצבי פתיחה:</b>
<code>"r" - קריאה
"w" - כתיבה (מחיקת תוכן קיים)
"a" - הוספה בסוף
"r+" - קריאה וכתיבה</code>
        """,
        "exercise": {
            "question": "איזה מצב פתיחה משמש לכתיבה לקובץ?",
            "answer": "w",
            "hint": "רמז: ראשית של write"
        }
    },
    14: {
        "title": "⚠️ טיפול בשגיאות",
        "content": """
<b>שיעור 14: Try-Except ⚠️</b>

לפעמים הקוד נכשל. צריך לטפל בזה!

<b>בעיה:</b>
<code>number = int("abc")  # שגיאה! 💥</code>

<b>פתרון - try-except:</b>
<code>try:
    number = int("abc")
    print(number)
except:
    print("לא הצלחתי להמיר למספר!")</code>

<b>לכידת סוג שגיאה ספציפי:</b>
<code>try:
    result = 10 / 0
except ZeroDivisionError:
    print("לא אפשר לחלק באפס!")</code>

<b>else ו-finally:</b>
<code>try:
    number = int("5")
except ValueError:
    print("שגיאה!")
else:
    print("הצלחה!")  # רק אם לא היתה שגיאה
finally:
    print("זה רץ תמיד")</code>

<b>שגיאות נפוצות:</b>
<code>ValueError - ערך לא תקין
TypeError - סוג נתון שגוי
KeyError - מפתח לא קיים במילון
IndexError - אינדקס מחוץ לטווח</code>
        """,
        "exercise": {
            "question": "איזו מילת מפתח תופסת שגיאות?",
            "answer": "except",
            "hint": "רמז: באנגלית 'חוץ מ' או 'למעט'"
        }
    },
    15: {
        "title": "📦 מודולים וספריות",
        "content": """
<b>שיעור 15: ייבוא מודולים 📦</b>

פייתון מגיעה עם המון כלים מובנים!

<b>ייבוא מודול:</b>
<code>import math

print(math.sqrt(16))  # 4.0
print(math.pi)  # 3.14159...</code>

<b>ייבוא פונקציה ספציפית:</b>
<code>from math import sqrt, pi

print(sqrt(25))  # 5.0
print(pi)  # 3.14159...</code>

<b>כינוי למודול:</b>
<code>import datetime as dt

now = dt.datetime.now()
print(now)</code>

<b>מודולים שימושיים:</b>
<code>random - מספרים אקראיים
datetime - תאריכים ושעות
json - עבודה עם JSON
os - פעולות מערכת
re - ביטויים רגולריים</code>

<b>דוגמה:</b>
<code>import random

number = random.randint(1, 10)
print(f"מספר אקראי: {number}")</code>
        """,
        "exercise": {
            "question": "איזו מילת מפתח מייבאת מודול?",
            "answer": "import",
            "hint": "רמז: באנגלית 'ייבוא'"
        }
    },
    16: {
        "title": "🎨 List Comprehension",
        "content": """
<b>שיעור 16: יצירת רשימות בקצרה 🎨</b>

דרך מהירה ויפה ליצור רשימות!

<b>הדרך הרגילה:</b>
<code>squares = []
for i in range(10):
    squares.append(i ** 2)
print(squares)</code>

<b>עם List Comprehension:</b>
<code>squares = [i ** 2 for i in range(10)]
print(squares)
# [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]</code>

<b>עם תנאי:</b>
<code># רק מספרים זוגיים
evens = [i for i in range(20) if i % 2 == 0]
print(evens)
# [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]</code>

<b>עם מחרוזות:</b>
<code>names = ["דני", "שרה", "יוסי"]
upper = [name.upper() for name in names]
print(upper)</code>

<b>מורכב יותר:</b>
<code># יצירת מילון
squares_dict = {i: i**2 for i in range(5)}
# {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}</code>

<b>למה להשתמש?</b>
✅ קוד קצר וברור
✅ מהיר יותר
✅ פייתוני!
        """,
        "exercise": {
            "question": "איך נקרא לדרך הקצרה ליצירת רשימה?",
            "answer": "list comprehension",
            "hint": "רמז: list comprehension"
        }
    },
    17: {
        "title": "🏗️ מחלקות - OOP בסיסי",
        "content": """
<b>שיעור 17: תכנות מונחה עצמים 🏗️</b>

מחלקה היא תבנית ליצירת אובייקטים.

<b>יצירת מחלקה:</b>
<code>class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def bark(self):
        print(f"{self.name} says: Woof!")

# יצירת אובייקט
my_dog = Dog("רקס", 5)
print(my_dog.name)  # רקס
my_dog.bark()  # רקס says: Woof!</code>

<b>למה מחלקות?</b>
✅ ארגון קוד טוב יותר
✅ שימוש חוזר
✅ מודל העולם האמיתי

<b>דוגמה - חשבון בנק:</b>
<code>class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance
    
    def deposit(self, amount):
        self.balance += amount
        print(f"הפקדת {amount}₪")
    
    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"משכת {amount}₪")
        else:
            print("אין מספיק כסף!")

account = BankAccount("דני", 1000)
account.deposit(500)
account.withdraw(300)
print(f"יתרה: {account.balance}₪")</code>
        """,
        "exercise": {
            "question": "איזו מילת מפתח מגדירה מחלקה?",
            "answer": "class",
            "hint": "רמז: באנגלית 'מחלקה'"
        }
    },
    18: {
        "title": "🔧 פונקציות Lambda",
        "content": """
<b>שיעור 18: פונקציות אנונימיות 🔧</b>

Lambda - פונקציה קצרה בשורה אחת!

<b>פונקציה רגילה:</b>
<code>def double(x):
    return x * 2

print(double(5))  # 10</code>

<b>עם Lambda:</b>
<code>double = lambda x: x * 2
print(double(5))  # 10</code>

<b>עם פרמטרים מרובים:</b>
<code>add = lambda x, y: x + y
print(add(3, 5))  # 8</code>

<b>שימוש עם map():</b>
<code>numbers = [1, 2, 3, 4, 5]
doubled = list(map(lambda x: x * 2, numbers))
print(doubled)  # [2, 4, 6, 8, 10]</code>

<b>שימוש עם filter():</b>
<code>numbers = [1, 2, 3, 4, 5, 6]
evens = list(filter(lambda x: x % 2 == 0, numbers))
print(evens)  # [2, 4, 6]</code>

<b>מיון עם sorted():</b>
<code>students = [("דני", 85), ("שרה", 92), ("יוסי", 78)]
sorted_students = sorted(students, key=lambda x: x[1])
print(sorted_students)
# [('יוסי', 78), ('דני', 85), ('שרה', 92)]</code>
        """,
        "exercise": {
            "question": "איזו מילת מפתח יוצרת פונקציה אנונימית?",
            "answer": "lambda",
            "hint": "רמז: lambda"
        }
    },
    19: {
        "title": "🎁 *args ו-**kwargs",
        "content": """
<b>שיעור 19: ארגומנטים משתנים 🎁</b>

איך מקבלים מספר לא ידוע של פרמטרים?

<b>*args - מספר משתנה של ארגומנטים:</b>
<code>def sum_all(*args):
    total = 0
    for num in args:
        total += num
    return total

print(sum_all(1, 2, 3))  # 6
print(sum_all(1, 2, 3, 4, 5))  # 15</code>

<b>**kwargs - מילון של ארגומנטים:</b>
<code>def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_info(name="דני", age=25, city="תל אביב")
# name: דני
# age: 25
# city: תל אביב</code>

<b>שילוב הכל:</b>
<code>def my_function(a, b, *args, **kwargs):
    print(f"a: {a}")
    print(f"b: {b}")
    print(f"args: {args}")
    print(f"kwargs: {kwargs}")

my_function(1, 2, 3, 4, 5, name="דני", age=25)
# a: 1
# b: 2
# args: (3, 4, 5)
# kwargs: {'name': 'דני', 'age': 25}</code>

<b>שימוש מעשי:</b>
<code>def greet(greeting, *names):
    for name in names:
        print(f"{greeting} {name}!")

greet("שלום", "דני", "שרה", "יוסי")
# שלום דני!
# שלום שרה!
# שלום יוסי!</code>
        """,
        "exercise": {
            "question": "מה מסמל * לפני שם פרמטר?",
            "answer": "args",
            "hint": "רמז: *args - מספר משתנה של ארגומנטים"
        }
    },
    20: {
        "title": "🎓 סיכום ומה הלאה",
        "content": """
<b>🎉 כל הכבוד! סיימת 20 שיעורים! 🎉</b>

<b>מה למדת עד עכשיו?</b>
✅ יסודות פייתון - משתנים, סוגי נתונים
✅ מבנים לוגיים - תנאים ולולאות
✅ מבני נתונים - רשימות, מילונים, טאפלים, סטים
✅ פונקציות - רגילות, lambda, args/kwargs
✅ קבצים - קריאה וכתיבה
✅ טיפול בשגיאות - try/except
✅ מודולים - ייבוא ושימוש
✅ OOP בסיסי - מחלקות
✅ טכניקות מתקדמות - list comprehension

<b>מה הלאה? 🚀</b>

<b>1. תרגול הרבה!</b>
💪 כתוב תוכניות קטנות
💪 פתור תרגילים באתרים כמו:
   • HackerRank
   • LeetCode
   • Codewars

<b>2. בחר התמחות:</b>
🌐 Web Development - Flask/Django
📊 Data Science - Pandas/NumPy
🤖 Automation - Selenium
🎮 Game Development - Pygame
🤖 AI/ML - TensorFlow

<b>3. פרויקטים אישיים:</b>
💡 בנה משהו שמעניין אותך!
💡 העלה ל-GitHub
💡 למד מטעויות

<b>משאבים מומלצים:</b>
📚 Python Documentation
📚 Real Python
📚 Automate the Boring Stuff
📚 Python Crash Course

<b>זכור:</b>
🌟 תכנות זה מיומנות - צריך תרגול!
🌟 כולם מתחילים כמתחילים
🌟 השגיאות זה חלק מהלמידה
🌟 הקהילה כאן לעזור!

<b>תודה שלמדת איתי! 💙</b>
המשך ללמוד, תרגל הרבה, ותהיה מתכנת מעולה! 🚀
        """,
        "exercise": {
            "question": "מה הצעד החשוב ביותר אחרי למידת פייתון?",
            "answer": "תרגול",
            "hint": "רמז: practice makes perfect!"
        }
    }
}

# ====================
# פונקציות עזר
# ====================

def load_user_progress():
    """טוען את התקדמות המשתמשים"""
    if os.path.exists(USER_DATA_FILE):
        with open(USER_DATA_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    return {}

def save_user_progress(data):
    """שומר את התקדמות המשתמשים"""
    with open(USER_DATA_FILE, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

def get_user_lesson(user_id):
    """מחזיר את מספר השיעור הנוכחי של המשתמש"""
    progress = load_user_progress()
    return progress.get(str(user_id), {}).get("current_lesson", 1)

def set_user_lesson(user_id, lesson_number):
    """מעדכן את מספר השיעור של המשתמש"""
    progress = load_user_progress()
    user_id_str = str(user_id)
    if user_id_str not in progress:
        progress[user_id_str] = {}
    progress[user_id_str]["current_lesson"] = lesson_number
    save_user_progress(progress)

def create_main_menu():
    """יוצר את התפריט הראשי"""
    keyboard = [
        [InlineKeyboardButton("📚 השיעור הנוכחי שלי", callback_data="current_lesson")],
        [InlineKeyboardButton("📖 רשימת כל השיעורים", callback_data="all_lessons")],
        [InlineKeyboardButton("📊 ההתקדמות שלי", callback_data="my_progress")],
        [InlineKeyboardButton("ℹ️ עזרה", callback_data="help")]
    ]
    return InlineKeyboardMarkup(keyboard)

def create_lesson_navigation(current_lesson, total_lessons):
    """יוצר כפתורי ניווט בין שיעורים"""
    keyboard = []
    nav_buttons = []
    
    if current_lesson > 1:
        nav_buttons.append(InlineKeyboardButton("⬅️ שיעור קודם", callback_data=f"lesson_{current_lesson-1}"))
    
    if current_lesson < total_lessons:
        nav_buttons.append(InlineKeyboardButton("שיעור הבא ➡️", callback_data=f"lesson_{current_lesson+1}"))
    
    if nav_buttons:
        keyboard.append(nav_buttons)
    
    keyboard.append([InlineKeyboardButton("✅ סיימתי! המשך לתרגיל", callback_data=f"exercise_{current_lesson}")])
    keyboard.append([InlineKeyboardButton("🏠 חזרה לתפריט", callback_data="main_menu")])
    
    return InlineKeyboardMarkup(keyboard)

# ====================
# Handlers
# ====================

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """פונקציה שרצה כש-/start נשלח"""
    user = update.effective_user
    user_id = user.id
    
    # אם זה משתמש חדש, שומרים אותו
    progress = load_user_progress()
    if str(user_id) not in progress:
        set_user_lesson(user_id, 1)
    
    welcome_text = f"""
🎓 <b>ברוך הבא ללימוד פייתון, {user.first_name}!</b>

אני הבוט שילמד אותך פייתון מאפס ועד גיבור! 🚀

<b>מה יש בקורס?</b>
📚 <b>20 שיעורים מקיפים</b> - מיסודות ועד מתקדם!
✏️ תרגילים אינטראקטיביים
🏆 מעקב אחר ההתקדמות שלך
🎯 למידה בקצב שלך

<b>נושאים בקורס:</b>
• יסודות - משתנים, סוגי נתונים
• לולאות ותנאים
• מבני נתונים - רשימות, מילונים
• פונקציות ו-OOP
• קבצים ומודולים
• ועוד הרבה!

<b>מוכן להתחיל?</b> לחץ על "השיעור הנוכחי שלי" 👇
    """
    
    await update.message.reply_text(
        welcome_text,
        parse_mode='HTML',
        reply_markup=create_main_menu()
    )

async def button_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """מטפל בלחיצות על כפתורים"""
    query = update.callback_query
    await query.answer()
    
    user_id = query.from_user.id
    data = query.data
    
    # תפריט ראשי
    if data == "main_menu":
        await query.edit_message_text(
            "🏠 <b>תפריט ראשי</b>\n\nמה תרצה לעשות?",
            parse_mode='HTML',
            reply_markup=create_main_menu()
        )
    
    # השיעור הנוכחי
    elif data == "current_lesson":
        current = get_user_lesson(user_id)
        if current in LESSONS:
            lesson = LESSONS[current]
            text = f"<b>{lesson['title']}</b>\n\n{lesson['content']}"
            await query.edit_message_text(
                text,
                parse_mode='HTML',
                reply_markup=create_lesson_navigation(current, len(LESSONS))
            )
        else:
            await query.edit_message_text(
                "🎉 <b>כל הכבוד!</b>\n\nסיימת את כל 20 השיעורים!\nאתה כבר מתכנת פייתון! 🚀\n\nהמשך לתרגל ולבנות פרויקטים! 💪",
                parse_mode='HTML',
                reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("🏠 תפריט ראשי", callback_data="main_menu")]])
            )
    
    # רשימת כל השיעורים
    elif data == "all_lessons":
        current = get_user_lesson(user_id)
        lessons_list = "<b>📖 רשימת השיעורים (20 שיעורים!):</b>\n\n"
        
        keyboard = []
        for num, lesson in LESSONS.items():
            status = "✅" if num < current else "🔒" if num > current else "▶️"
            lessons_list += f"{status} {lesson['title']}\n"
            
            # מאפשר גישה רק לשיעורים שכבר עברו או הנוכחי
            if num <= current:
                keyboard.append([InlineKeyboardButton(f"{status} שיעור {num}", callback_data=f"lesson_{num}")])
        
        keyboard.append([InlineKeyboardButton("🏠 תפריט ראשי", callback_data="main_menu")])
        
        await query.edit_message_text(
            lessons_list,
            parse_mode='HTML',
            reply_markup=InlineKeyboardMarkup(keyboard)
        )
    
    # צפייה בשיעור ספציפי
    elif data.startswith("lesson_"):
        lesson_num = int(data.split("_")[1])
        current = get_user_lesson(user_id)
        
        # בודק שהמשתמש הגיע לשיעור הזה
        if lesson_num <= current and lesson_num in LESSONS:
            lesson = LESSONS[lesson_num]
            text = f"<b>{lesson['title']}</b>\n\n{lesson['content']}"
            await query.edit_message_text(
                text,
                parse_mode='HTML',
                reply_markup=create_lesson_navigation(lesson_num, len(LESSONS))
            )
        else:
            await query.answer("🔒 תחילה סיים את השיעורים הקודמים!", show_alert=True)
    
    # תרגיל
    elif data.startswith("exercise_"):
        lesson_num = int(data.split("_")[1])
        
        if lesson_num in LESSONS:
            exercise = LESSONS[lesson_num]["exercise"]
            context.user_data['waiting_for_answer'] = lesson_num
            
            text = f"""
📝 <b>תרגיל - {LESSONS[lesson_num]['title']}</b>

<b>שאלה:</b>
{exercise['question']}

💡 שלח את התשובה שלך בהודעה...
(רוצה רמז? שלח "רמז")
            """
            
            keyboard = [[InlineKeyboardButton("🏠 חזרה לתפריט", callback_data="main_menu")]]
            
            await query.edit_message_text(
                text,
                parse_mode='HTML',
                reply_markup=InlineKeyboardMarkup(keyboard)
            )
    
    # התקדמות
    elif data == "my_progress":
        current = get_user_lesson(user_id)
        total = len(LESSONS)
        completed = current - 1
        percentage = (completed / total) * 100
        
        stars = min(5, completed // 4)
        empty_stars = 5 - stars
        
        progress_text = f"""
📊 <b>ההתקדמות שלך</b>

🎯 שיעורים שסיימת: {completed}/{total}
📈 אחוזי התקדמות: {percentage:.1f}%

{"🌟" * stars}{"⭐" * empty_stars}

{get_progress_message(completed, total)}
        """
        
        await query.edit_message_text(
            progress_text,
            parse_mode='HTML',
            reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("🏠 תפריט ראשי", callback_data="main_menu")]])
        )
    
    # עזרה
    elif data == "help":
        help_text = """
ℹ️ <b>איך להשתמש בבוט?</b>

<b>📚 השיעור הנוכחי שלי</b>
עבור לשיעור שאתה נמצא בו כרגע

<b>📖 רשימת כל השיעורים</b>
ראה את כל 20 השיעורים

<b>📊 ההתקדמות שלי</b>
בדוק כמה שיעורים סיימת

<b>💡 טיפים:</b>
• יש 20 שיעורים מקיפים!
• כל שיעור מסתיים בתרגיל
• אי אפשר לדלג על שיעורים
• לומדים בקצב שלך
• תמיד אפשר לחזור לשיעורים קודמים

<b>נושאים בקורס:</b>
1-5: יסודות פייתון
6-10: לולאות, תנאים, מבני נתונים
11-15: קבצים, שגיאות, מודולים
16-20: טכניקות מתקדמות

<b>זקוק לעזרה?</b> פשוט שלח הודעה!
        """
        
        await query.edit_message_text(
            help_text,
            parse_mode='HTML',
            reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("🏠 תפריט ראשי", callback_data="main_menu")]])
        )

def get_progress_message(completed, total):
    """מחזיר הודעת עידוד לפי התקדמות"""
    if completed == 0:
        return "💪 בוא נתחיל ללמוד!"
    elif completed < 5:
        return "🎉 התחלה נהדרת! המשך כך!"
    elif completed < 10:
        return "🚀 אתה בדרך הנכונה!"
    elif completed < 15:
        return "⭐ מעולה! אתה כבר יודע הרבה!"
    elif completed < 20:
        return "🏆 כמעט סיימת! עוד קצת!"
    else:
        return "🎓 מדהים! סיימת את כל הקורס!"

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """מטפל בהודעות טקסט (תשובות לתרגילים)"""
    user_id = update.effective_user.id
    text = update.message.text.strip()
    
    # בודק אם המשתמש באמצע תרגיל
    if 'waiting_for_answer' in context.user_data:
        lesson_num = context.user_data['waiting_for_answer']
        exercise = LESSONS[lesson_num]["exercise"]
        
        # בקשה לרמז
        if text.lower() in ["רמז", "hint"]:
            await update.message.reply_text(
                f"💡 {exercise['hint']}\n\nנסה שוב!",
                parse_mode='HTML'
            )
            return
        
        # בדיקת תשובה
        correct_answer = exercise['answer'].lower().strip()
        user_answer = text.lower().strip()
        
        if user_answer == correct_answer or correct_answer in user_answer:
            # תשובה נכונה!
            current = get_user_lesson(user_id)
            if lesson_num >= current:
                set_user_lesson(user_id, lesson_num + 1)
            
            del context.user_data['waiting_for_answer']
            
            # הודעת ברכה מיוחדת אם סיים את הקורס
            if lesson_num == len(LESSONS):
                congrats_text = f"""
🎉🎉🎉 <b>מדהים! תשובה נכונה!</b> 🎉🎉🎉

התשובה הנכונה היא: <code>{exercise['answer']}</code>

🏆🏆🏆 <b>סיימת את כל 20 השיעורים!</b> 🏆🏆🏆

אתה עכשיו מכיר את:
✅ כל יסודות פייתון
✅ לולאות ותנאים
✅ מבני נתונים
✅ פונקציות ו-OOP
✅ קבצים ומודולים
✅ טכניקות מתקדמות

<b>מה הלאה?</b>
🚀 תרגל! בנה פרויקטים!
📚 למד ספריות מתקדמות
💼 התחל לפתח דברים אמיתיים!

כל הכבוד! אתה מתכנת פייתון! 💙🐍
                """
            else:
                congrats_text = f"""
🎉 <b>מעולה! תשובה נכונה!</b> ✅

התשובה הנכונה היא: <code>{exercise['answer']}</code>

{"🏆 עברת לשיעור הבא!" if lesson_num >= current else ""}

מה תרצה לעשות עכשיו?
                """
            
            keyboard = []
            if lesson_num < len(LESSONS):
                keyboard.append([InlineKeyboardButton("➡️ השיעור הבא", callback_data=f"lesson_{lesson_num+1}")])
            keyboard.append([InlineKeyboardButton("📖 כל השיעורים", callback_data="all_lessons")])
            keyboard.append([InlineKeyboardButton("🏠 תפריט ראשי", callback_data="main_menu")])
            
            await update.message.reply_text(
                congrats_text,
                parse_mode='HTML',
                reply_markup=InlineKeyboardMarkup(keyboard)
            )
        else:
            # תשובה שגויה
            await update.message.reply_text(
                f"❌ <b>לא מדויק...</b>\n\nנסה שוב! 💪\n(כתוב 'רמז' אם אתה תקוע)",
                parse_mode='HTML'
            )
    else:
        # הודעה רגילה - מציע תפריט
        await update.message.reply_text(
            "היי! 👋\n\nאשמח לעזור לך ללמוד פייתון.\nהשתמש בכפתורים בתפריט למטה:",
            reply_markup=create_main_menu()
        )

# ====================
# Main
# ====================

def main():
    """נקודת הכניסה של הבוט"""
    print("🤖 הבוט מתחיל...")
    print(f"📚 טוען {len(LESSONS)} שיעורים...")
    
    # יצירת האפליקציה
    application = Application.builder().token(BOT_TOKEN).build()
    
    # הוספת handlers
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CallbackQueryHandler(button_callback))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    
    print("✅ הבוט פועל! לחץ Ctrl+C לעצירה.")
    print(f"🎓 הקורס כולל {len(LESSONS)} שיעורים מיסודות ועד מתקדם!")
    
    # הרצת הבוט
    application.run_polling(allowed_updates=Update.ALL_TYPES)

if __name__ == "__main__":
    main()
