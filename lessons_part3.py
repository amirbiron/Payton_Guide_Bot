# -*- coding: utf-8 -*-
"""
המשך השיעורים - חלק 3
שיעורים 11-15
"""

LESSONS_PART3 = {
    11: {
        'title': '📖 שיעור 11: Dictionaries - מילונים',
        'content': """
מילונים הם אחד הכלים הכי עוצמתיים ב-Python! 🗂️

🎯 <b>מה זה Dictionary?</b>
מילון (dict) הוא אוסף של זוגות מפתח-ערך. כמו מילון אמיתי: מילה (מפתח) ← הגדרה (ערך)!

📝 <b>יצירת מילון:</b>
<code>student = {
    "name": "אמיר",
    "age": 20,
    "grade": 95
}

empty = {}  # מילון רי ק
capitals = {"ישראל": "ירושלים", "צרפת": "פריז"}</code>

📍 <b>גישה לערכים:</b>
<code>student = {"name": "דני", "age": 22}
print(student["name"])  # דני
print(student["age"])   # 22

# דרך בטוחה יותר:
print(student.get("name"))      # דני
print(student.get("city", "לא קיים"))  # לא קיים</code>

get לא יוצר שגיאה אם המפתח לא קיים!

✏️ <b>הוספה ועדכון:</b>
<code>person = {"name": "יוסי"}

# הוספת מפתח חדש:
person["age"] = 25
print(person)  # {"name": "יוסי", "age": 25}

# עדכון ערך קיים:
person["age"] = 26
print(person)  # {"name": "יוסי", "age": 26}</code>

❌ <b>מחיקת פריטים:</b>
<code>car = {"brand": "טויוטה", "year": 2020, "color": "שחור"}

# מחיקת מפתח:
del car["color"]
print(car)  # {"brand": "טויוטה", "year": 2020}

# מחיקה עם החזרת ערך:
year = car.pop("year")
print(year)  # 2020</code>

🔍 <b>בדיקה אם מפתח קיים:</b>
<code>user = {"name": "אלי", "age": 30}

if "name" in user:
    print("יש שם!")

if "email" not in user:
    print("אין אימייל")</code>

📊 <b>קבלת מפתחות, ערכים וזוגות:</b>
<code>scores = {"מתמטיקה": 90, "אנגלית": 85}

# כל המפתחות:
print(scores.keys())    # dict_keys(['מתמטיקה', 'אנגלית'])

# כל הערכים:
print(scores.values())  # dict_values([90, 85])

# כל הזוגות:
print(scores.items())   # dict_items([('מתמטיקה', 90), ('אנגלית', 85)])</code>

🔁 <b>לולאה על מילון:</b>
<code>grades = {"מתמטיקה": 90, "אנגלית": 85, "היסטוריה": 88}

# רק מפתחות:
for subject in grades:
    print(subject)

# מפתחות וערכים:
for subject, grade in grades.items():
    print(f"{subject}: {grade}")

# רק ערכים:
for grade in grades.values():
    print(grade)</code>

📏 <b>אורך מילון:</b>
<code>data = {"a": 1, "b": 2, "c": 3}
print(len(data))  # 3</code>

🔄 <b>העתקת מילון:</b>
<code>original = {"x": 10, "y": 20}
copy = original.copy()
copy["z"] = 30
print(original)  # {"x": 10, "y": 20}
print(copy)      # {"x": 10, "y": 20, "z": 30}</code>

➕ <b>מיזוג מילונים:</b>
<code>dict1 = {"a": 1, "b": 2}
dict2 = {"c": 3, "d": 4}

# Python 3.9+:
merged = dict1 | dict2
print(merged)  # {"a": 1, "b": 2, "c": 3, "d": 4}

# דרך ישנה יותר:
dict1.update(dict2)
print(dict1)  # {"a": 1, "b": 2, "c": 3, "d": 4}</code>

🎯 <b>מילונים מקוננים:</b>
<code>school = {
    "class_a": {
        "students": 30,
        "teacher": "מר כהן"
    },
    "class_b": {
        "students": 28,
        "teacher": "גב' לוי"
    }
}

print(school["class_a"]["teacher"])  # מר כהן</code>

💡 <b>ערכים ברירת מחדל:</b>
<code>counter = {}
words = ["תפוח", "בננה", "תפוח", "תפוז", "בננה"]

for word in words:
    counter[word] = counter.get(word, 0) + 1

print(counter)  # {"תפוח": 2, "בננה": 2, "תפוז": 1}</code>

🎨 <b>Dictionary Comprehension:</b>
<code># ריבועים:
squares = {x: x**2 for x in range(5)}
print(squares)  # {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}

# המרת רשימה:
names = ["אמיר", "דני", "יוסי"]
ids = {name: i for i, name in enumerate(names)}
print(ids)  # {"אמיר": 0, "דני": 1, "יוסי": 2}</code>

🔥 <b>דוגמה מעשית - מערכת משתמשים:</b>
<code>users = {
    "user001": {
        "name": "אמיר",
        "email": "amir@example.com",
        "role": "admin"
    },
    "user002": {
        "name": "דני",
        "email": "danny@example.com",
        "role": "user"
    }
}

# קבלת מידע על משתמש:
user_id = "user001"
if user_id in users:
    print(f"שם: {users[user_id]['name']}")
    print(f"תפקיד: {users[user_id]['role']}")</code>

📚 <b>מתי להשתמש ב-Dictionary?</b>
• כשצריך לגשת לנתונים לפי מפתח ייחודי
• לאחסון הגדרות
• למידע מובנה (כמו JSON)
• למיפוי בין דברים
""",
        'exercise': {
            'question': 'מה יודפס?\n\ndata = {"a": 1, "b": 2}\ndata["c"] = 3\nprint(len(data))',
            'options': ['2', '3', '6', 'שגיאה'],
            'correct_answer': '3',
            'explanation': 'נכון! 👏 התחלנו עם 2 זוגות, הוספנו עוד אחד, אז len מחזיר 3'
        }
    },
    
    12: {
        'title': '⚡ שיעור 12: פונקציות - קוד לשימוש חוזר',
        'content': """
פונקציות הן הלב של תכנות טוב! בואו נלמד איך לכתוב אותן! 🎯

🎯 <b>מה זו פונקציה?</b>
פונקציה היא בלוק של קוד שאפשר להפעיל שוב ושוב עם קלות!

📝 <b>פונקציה בסיסית:</b>
<code>def say_hello():
    print("שלום!")

# הפעלת הפונקציה:
say_hello()  # שלום!</code>

💡 <b>מבנה פונקציה:</b>
• def - מילה שמורה להגדרת פונקציה
• שם הפונקציה
• סוגריים ()
• נקודותיים :
• הקוד (מזוזז פנימה)

📊 <b>פונקציה עם פרמטרים:</b>
<code>def greet(name):
    print(f"שלום {name}!")

greet("אמיר")  # שלום אמיר!
greet("דני")   # שלום דני!</code>

🎯 <b>כמה פרמטרים:</b>
<code>def add_numbers(a, b):
    result = a + b
    print(f"{a} + {b} = {result}")

add_numbers(5, 3)   # 5 + 3 = 8
add_numbers(10, 20) # 10 + 20 = 30</code>

↩️ <b>החזרת ערך - return:</b>
<code>def multiply(a, b):
    return a * b

result = multiply(4, 5)
print(result)  # 20

# שימוש ישיר:
print(multiply(3, 7))  # 21</code>

💡 <b>return עוצר את הפונקציה!</b>
<code>def check_age(age):
    if age < 18:
        return "קטין"
    return "מבוגר"

print(check_age(15))  # קטין
print(check_age(25))  # מבוגר</code>

🎨 <b>ערכי ברירת מחדל:</b>
<code>def greet(name, greeting="שלום"):
    print(f"{greeting} {name}!")

greet("אמיר")           # שלום אמיר!
greet("דני", "היי")     # היי דני!</code>

📚 <b>החזרת כמה ערכים:</b>
<code>def get_stats(numbers):
    total = sum(numbers)
    average = total / len(numbers)
    return total, average

sum_val, avg_val = get_stats([10, 20, 30])
print(f"סכום: {sum_val}, ממוצע: {avg_val}")</code>

⭐ <b>*args - מספר משתנה של פרמטרים:</b>
<code>def add_all(*numbers):
    return sum(numbers)

print(add_all(1, 2, 3))        # 6
print(add_all(10, 20, 30, 40)) # 100</code>

🎯 <b>**kwargs - פרמטרים עם שמות:</b>
<code>def print_info(**info):
    for key, value in info.items():
        print(f"{key}: {value}")

print_info(name="אמיר", age=25, city="תל אביב")</code>

💪 <b>docstring - תיעוד פונקציה:</b>
<code>def calculate_area(width, height):
      '''
      מחשב שטח מלבן.
      
      Args:
          width: רוחב המלבן
          height: גובה המלבן
      
      Returns:
          שטח המלבן
      '''
    return width * height

# גישה לתיעוד:
print(calculate_area.__doc__)</code>

🔁 <b>פונקציות רקורסיביות:</b>
<code>def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

print(factorial(5))  # 120</code>

🎯 <b>פונקציות כאובייקטים:</b>
<code>def square(x):
    return x ** 2

def cube(x):
    return x ** 3

operations = [square, cube]
for op in operations:
    print(op(3))  # 9, 27</code>

🔥 <b>Lambda - פונקציות קצרות:</b>
<code>square = lambda x: x ** 2
print(square(5))  # 25

# עם sort:
points = [(1, 2), (3, 1), (5, 4)]
points.sort(key=lambda p: p[1])
print(points)  # [(3, 1), (1, 2), (5, 4)]</code>

💡 <b>scope - תחום משתנים:</b>
<code>x = 10  # משתנה גלובלי

def my_function():
    x = 5  # משתנה לוקלי
    print(x)  # 5

my_function()
print(x)  # 10

# שינוי משתנה גלובלי:
def change_global():
    global x
    x = 20

change_global()
print(x)  # 20</code>

🎨 <b>דוגמה מעשית - מחשבון:</b>
<code>def calculator(a, b, operation):
    if operation == "+":
        return a + b
    elif operation == "-":
        return a - b
    elif operation == "*":
        return a * b
    elif operation == "/":
        if b != 0:
            return a / b
        return "שגיאה: חילוק באפס"
    return "פעולה לא ידועה"

print(calculator(10, 5, "+"))  # 15
print(calculator(10, 5, "*"))  # 50</code>

📚 <b>טיפים חשובים:</b>
• תנו לפונקציות שמות תיאוריים
• כל פונקציה צריכה לעשות דבר אחד טוב
• תכתבו תיעוד לפונקציות מורכבות
• השתמשו ב-return במקום print בפונקציות
""",
        'exercise': {
            'question': 'מה יודפס?\n\ndef double(x):\n    return x * 2\n\nresult = double(5)\nprint(result)',
            'options': ['5', '10', '52', 'שגיאה'],
            'correct_answer': '10',
            'explanation': 'מצוין! 🎯 הפונקציה double מכפילה את 5 ב-2 ומחזירה 10'
        }
    },
    
    13: {
        'title': '📂 שיעור 13: עבודה עם קבצים',
        'content': """
בואו נלמד איך לקרוא ולכתוב קבצים! 📝

🎯 <b>למה לעבוד עם קבצים?</b>
קבצים מאפשרים לשמור מידע גם אחרי שהתוכנית נסגרת!

📖 <b>קריאת קובץ טקסט:</b>
<code># פתיחה וקריאה:
file = open("data.txt", "r", encoding="utf-8")
content = file.read()
print(content)
file.close()  # חשוב לסגור!</code>

✨ <b>דרך יותר טובה - with:</b>
<code>with open("data.txt", "r", encoding="utf-8") as file:
    content = file.read()
    print(content)
# הקובץ נסגר אוטומטית!</code>

📝 <b>מצבי פתיחה:</b>
<code>"r"  # קריאה (read)
"w"  # כתיבה (write) - מוחק תוכן קיים!
"a"  # הוספה (append) - מוסיף לסוף
"r+" # קריאה וכתיבה
"x"  # יצירה - שגיאה אם הקובץ קיים</code>

✍️ <b>כתיבה לקובץ:</b>
<code>with open("output.txt", "w", encoding="utf-8") as file:
    file.write("שורה ראשונה\n")
    file.write("שורה שנייה\n")</code>

⚠️ <b>w מוחק את כל התוכן הקיים!</b>

➕ <b>הוספה לקובץ קיים:</b>
<code>with open("log.txt", "a", encoding="utf-8") as file:
    file.write("רשומה חדשה\n")</code>

📄 <b>קריאת שורות:</b>
<code># כל השורות כרשימה:
with open("data.txt", "r", encoding="utf-8") as file:
    lines = file.readlines()
    for line in lines:
        print(line.strip())  # strip מסיר \n

# שורה אחת בכל פעם:
with open("data.txt", "r", encoding="utf-8") as file:
    for line in file:
        print(line.strip())</code>

🔢 <b>קריאת שורה ספציפית:</b>
<code>with open("data.txt", "r", encoding="utf-8") as file:
    first_line = file.readline()
    second_line = file.readline()
    print(first_line, second_line)</code>

🎯 <b>בדיקה אם קובץ קיים:</b>
<code>import os

if os.path.exists("data.txt"):
    print("הקובץ קיים!")
else:
    print("הקובץ לא קיים")</code>

📊 <b>מידע על קובץ:</b>
<code>import os

# גודל קובץ:
size = os.path.getsize("data.txt")
print(f"גודל: {size} bytes")

# בדיקה אם זה קובץ או תיקייה:
print(os.path.isfile("data.txt"))  # True
print(os.path.isdir("data.txt"))   # False</code>

🗑️ <b>מחיקת קובץ:</b>
<code>import os

if os.path.exists("temp.txt"):
    os.remove("temp.txt")
    print("הקובץ נמחק")</code>

📁 <b>עבודה עם תיקיות:</b>
<code>import os

# יצירת תיקייה:
os.mkdir("new_folder")

# קבלת רשימת קבצים:
files = os.listdir(".")
print(files)

# מחיקת תיקייה:
os.rmdir("new_folder")  # רק אם ריקה!</code>

💾 <b>עבודה עם JSON:</b>
<code>import json

# כתיבה ל-JSON:
data = {
    "name": "אמיר",
    "age": 25,
    "hobbies": ["תכנות", "קריאה"]
}

with open("data.json", "w", encoding="utf-8") as file:
    json.dump(data, file, ensure_ascii=False, indent=2)

# קריאה מ-JSON:
with open("data.json", "r", encoding="utf-8") as file:
    loaded_data = json.load(file)
    print(loaded_data["name"])</code>

📋 <b>עבודה עם CSV:</b>
<code>import csv

# כתיבה ל-CSV:
data = [
    ["שם", "גיל", "עיר"],
    ["אמיר", "25", "תל אביב"],
    ["דני", "30", "חיפה"]
]

with open("data.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerows(data)

# קריאה מ-CSV:
with open("data.csv", "r", encoding="utf-8") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)</code>

🔥 <b>טיפול בשגיאות:</b>
<code>try:
    with open("nonexistent.txt", "r") as file:
        content = file.read()
except FileNotFoundError:
    print("הקובץ לא נמצא!")
except PermissionError:
    print("אין הרשאות לקרוא את הקובץ!")</code>

💡 <b>דוגמה מעשית - ספירת מילים:</b>
<code>def count_words(filename):
    try:
        with open(filename, "r", encoding="utf-8") as file:
            content = file.read()
            words = content.split()
            return len(words)
    except FileNotFoundError:
        return "הקובץ לא נמצא"

result = count_words("article.txt")
print(f"מספר מילים: {result}")</code>

📚 <b>טיפים חשובים:</b>
• תמיד השתמשו ב-with לעבודה עם קבצים
• תמיד ציינו encoding="utf-8" לעברית
• אל תשכחו לטפל בשגיאות
• שמרו גיבויים לפני שינוי קבצים!
""",
        'exercise': {
            'question': 'איזה מצב פתיחה מוסיף תוכן לסוף קובץ קיים?',
            'options': ['"r"', '"w"', '"a"', '"x"'],
            'correct_answer': '"a"',
            'explanation': 'נכון! 🎉 "a" (append) מוסיף תוכן לסוף הקובץ בלי למחוק את התוכן הקיים'
        }
    },
    
    14: {
        'title': '⚠️ שיעור 14: טיפול בשגיאות - Try/Except',
        'content': """
שגיאות הן חלק מהתכנות - בואו נלמד להתמודד איתן! 🛡️

🎯 <b>למה צריך טיפול בשגיאות?</b>
כדי שהתוכנית לא תקרוס כשמשהו משתבש!

💥 <b>שגיאה בסיסית:</b>
<code># זה יקרוס:
number = int("abc")  # ValueError!
print("זה לא יודפס...")</code>

✅ <b>try-except בסיסי:</b>
<code>try:
    number = int("abc")
    print(number)
except:
    print("משהו השתבש!")</code>

🎯 <b>תפיסת שגיאה ספציפית:</b>
<code>try:
    number = int("abc")
except ValueError:
    print("זה לא מספר תקין!")</code>

💡 <b>סוגי שגיאות נפוצים:</b>
<code># ValueError - ערך לא תקין:
try:
    int("abc")
except ValueError:
    print("ערך לא תקין")

# ZeroDivisionError - חילוק באפס:
try:
    result = 10 / 0
except ZeroDivisionError:
    print("אי אפשר לחלק באפס!")

# IndexError - אינדקס לא קיים:
try:
    numbers = [1, 2, 3]
    print(numbers[10])
except IndexError:
    print("האינדקס לא קיים")

# KeyError - מפתח לא קיים:
try:
    data = {"name": "אמיר"}
    print(data["age"])
except KeyError:
    print("המפתח לא קיים")

# FileNotFoundError - קובץ לא נמצא:
try:
    file = open("nonexistent.txt")
except FileNotFoundError:
    print("הקובץ לא נמצא")</code>

🔄 <b>כמה except:</b>
<code>try:
    num = int(input("הכנס מספר: "))
    result = 10 / num
    print(result)
except ValueError:
    print("זה לא מספר!")
except ZeroDivisionError:
    print("אפס? ברצינות?")
except Exception as e:
    print(f"שגיאה אחרת: {e}")</code>

💬 <b>קבלת הודעת השגיאה:</b>
<code>try:
    int("abc")
except ValueError as e:
    print(f"שגיאה: {e}")</code>

✨ <b>else - אם לא היתה שגיאה:</b>
<code>try:
    number = int("10")
except ValueError:
    print("שגיאה בהמרה")
else:
    print(f"הצלחה! המספר הוא {number}")</code>

🏁 <b>finally - תמיד רץ:</b>
<code>try:
    file = open("data.txt")
    # עבוד עם הקובץ
except FileNotFoundError:
    print("קובץ לא נמצא")
finally:
    print("זה תמיד רץ!")
    # סגור קובץ, נקה משאבים וכו'</code>

🎯 <b>שרשור try-except:</b>
<code>def safe_divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "לא ניתן לחלק באפס"
    except TypeError:
        return "ערכים לא תקינים"

print(safe_divide(10, 2))   # 5.0
print(safe_divide(10, 0))   # לא ניתן לחלק באפס
print(safe_divide(10, "a")) # ערכים לא תקינים</code>

🔥 <b>raise - זריקת שגיאה ידנית:</b>
<code>def validate_age(age):
    if age < 0:
        raise ValueError("גיל לא יכול להיות שלילי!")
    if age > 150:
        raise ValueError("גיל לא ריאלי!")
    return True

try:
    validate_age(-5)
except ValueError as e:
    print(e)  # גיל לא יכול להיות שלילי!</code>

🎨 <b>שגיאות מותאמות אישית:</b>
<code>class AgeError(Exception):
    pass

def check_voting_age(age):
    if age < 18:
        raise AgeError("צעיר מדי להצביע!")
    return True

try:
    check_voting_age(15)
except AgeError as e:
    print(e)</code>

💪 <b>דוגמה מעשית - קלט בטוח:</b>
<code>def get_number(prompt):
    while True:
        try:
            value = int(input(prompt))
            return value
        except ValueError:
            print("בבקשה הכנס מספר תקין!")

age = get_number("מה הגיל שלך? ")
print(f"אתה בן {age}")</code>

🎯 <b>טיפול בשגיאות בפונקציות:</b>
<code>def read_file_safe(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            return f.read()
    except FileNotFoundError:
        print(f"הקובץ {filename} לא נמצא")
        return None
    except PermissionError:
        print("אין הרשאות לקרוא את הקובץ")
        return None
    except Exception as e:
        print(f"שגיאה לא צפויה: {e}")
        return None

content = read_file_safe("data.txt")
if content:
    print(content)</code>

📊 <b>logging - תיעוד שגיאות:</b>
<code>import logging

logging.basicConfig(level=logging.ERROR)

try:
    result = 10 / 0
except ZeroDivisionError as e:
    logging.error(f"שגיאה: {e}")
    print("אירעה שגיאה, אבל ממשיכים...")</code>

⚡ <b>assert - וידוא תנאים:</b>
<code>def calculate_average(numbers):
    assert len(numbers) > 0, "הרשימה לא יכולה להיות ריקה!"
    return sum(numbers) / len(numbers)

try:
    avg = calculate_average([])
except AssertionError as e:
    print(e)</code>

📚 <b>טיפים חשובים:</b>
• תפסו שגיאות ספציפיות, לא רק Exception כללי
• אל תשתיקו שגיאות - תמיד תעשו משהו
• השתמשו ב-finally לניקוי משאבים
• תתעדו שגיאות בייצור (logging)
• אל תשתמשו ב-try-except לבקרת זרימה רגילה
""",
        'exercise': {
            'question': 'איזה בלוק תמיד רץ, גם אם הייתה שגיאה וגם אם לא?',
            'options': ['try', 'except', 'else', 'finally'],
            'correct_answer': 'finally',
            'explanation': 'נכון מאוד! 🎯 finally תמיד רץ, בלי קשר לשגיאות. שימושי לניקוי משאבים!'
        }
    },
    
    15: {
        'title': '📦 שיעור 15: מודולים וספריות',
        'content': """
בואו נלמד איך להשתמש בקוד של אחרים ולארגן את הקוד שלנו! 📚

🎯 <b>מה זה מודול?</b>
מודול הוא קובץ Python שמכיל קוד שאפשר להשתמש בו שוב ושוב!

📥 <b>import בסיסי:</b>
<code>import math

print(math.pi)        # 3.141592...
print(math.sqrt(16))  # 4.0</code>

🎨 <b>import עם כינוי:</b>
<code>import math as m

print(m.pi)
print(m.sqrt(25))  # 5.0</code>

⭐ <b>import פונקציה ספציפית:</b>
<code>from math import sqrt, pi

print(sqrt(9))  # 3.0
print(pi)       # 3.141592...</code>

💡 <b>import הכל (לא מומלץ!):</b>
<code>from math import *
# עכשיו הכל זמין ישירות
print(sqrt(4))  # 2.0</code>

📚 <b>מודולים מובנים שימושיים:</b>
<code># random - מספרים אקראיים:
import random
print(random.randint(1, 10))      # מספר אקראי בין 1-10
print(random.choice(['א', 'ב', 'ג']))  # בחירה אקראית

# datetime - תאריך ושעה:
from datetime import datetime
now = datetime.now()
print(now.strftime("%Y-%m-%d %H:%M"))

# time - זמן:
import time
print("מתחיל...")
time.sleep(2)  # המתן 2 שניות
print("סיום!")

# os - מערכת הפעלה:
import os
print(os.getcwd())  # תיקייה נוכחית
files = os.listdir(".")  # רשימת קבצים

# sys - מערכת Python:
import sys
print(sys.version)  # גרסת Python</code>

🔢 <b>math - מתמטיקה:</b>
<code>import math

print(math.ceil(4.3))   # 5 (עיגול למעלה)
print(math.floor(4.7))  # 4 (עיגול למטה)
print(math.pow(2, 3))   # 8.0
print(math.factorial(5)) # 120
print(math.sin(math.pi/2))  # 1.0</code>

🎲 <b>random - אקראיות:</b>
<code>import random

# מספר אקראי:
print(random.random())  # 0.0 - 1.0
print(random.uniform(1, 10))  # float בין 1-10

# רשימה:
numbers = [1, 2, 3, 4, 5]
random.shuffle(numbers)  # ערבוב במקום
print(numbers)

# דגימה:
selected = random.sample([1, 2, 3, 4, 5], 3)
print(selected)  # 3 מספרים אקראיים</code>

📅 <b>datetime - תאריך ושעה:</b>
<code>from datetime import datetime, timedelta

# זמן נוכחי:
now = datetime.now()
print(now)

# פורמט מותאם:
print(now.strftime("%d/%m/%Y"))
print(now.strftime("%H:%M:%S"))

# חישובי זמן:
tomorrow = now + timedelta(days=1)
next_week = now + timedelta(weeks=1)
print(f"מחר: {tomorrow.strftime('%d/%m/%Y')}")</code>

🔧 <b>יצירת מודול משלך:</b>

קובץ: my_module.py
<code># my_module.py
def greet(name):
    return f"שלום {name}!"

def add(a, b):
    return a + b

PI = 3.14159</code>

קובץ: main.py
<code># main.py
import my_module

print(my_module.greet("אמיר"))
print(my_module.add(5, 3))
print(my_module.PI)</code>

📁 <b>ארגון בחבילות (packages):</b>
<code>my_package/
    __init__.py
    module1.py
    module2.py

# שימוש:
from my_package import module1
from my_package.module2 import some_function</code>

💎 <b>pip - התקנת ספריות חיצוניות:</b>
<code># בטרמינל:
pip install requests
pip install numpy
pip install pandas

# בקוד:
import requests
response = requests.get("https://api.example.com")
print(response.json())</code>

🎯 <b>ספריות פופולריות:</b>
<code># requests - בקשות HTTP:
import requests
r = requests.get("https://api.github.com")
print(r.status_code)

# json - עבודה עם JSON:
import json
data = {"name": "אמיר", "age": 25}
json_string = json.dumps(data)
loaded_data = json.loads(json_string)

# collections - מבני נתונים מתקדמים:
from collections import Counter
words = ["תפוח", "בננה", "תפוח", "תפוז"]
counter = Counter(words)
print(counter)  # Counter({'תפוח': 2, ...})</code>

🔍 <b>dir() - מה יש במודול:</b>
<code>import math
print(dir(math))  # רשימת כל הפונקציות

# עזרה על פונקציה:
help(math.sqrt)</code>

⚡ <b>__name__ == "__main__":</b>
<code># my_script.py
def main():
    print("זה הסקריפט הראשי!")

if __name__ == "__main__":
    main()  # רק אם מריצים את הקובץ ישירות</code>

זה מאפשר לקובץ להיות גם מודול וגם סקריפט!

🎨 <b>דוגמה מעשית - מחולל סיסמאות:</b>
<code>import random
import string

def generate_password(length=12):
    characters = string.ascii_letters + string.digits + "!@#$%"
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

print(generate_password())
print(generate_password(16))</code>

📚 <b>טיפים חשובים:</b>
• השתמשו במודולים כדי לא לכתוב קוד מחדש
• תתעדו את המודולים שלכם
• השתמשו ב-requirements.txt לניהול תלויות
• קראו תיעוד של ספריות לפני שימוש
• אל תשכחו לעדכן ספריות (pip install --upgrade)
""",
        'exercise': {
            'question': 'איך מייבאים רק את הפונקציה sqrt ממודול math?',
            'options': ['import sqrt', 'from math import sqrt', 'import math.sqrt', 'sqrt from math'],
            'correct_answer': 'from math import sqrt',
            'explanation': 'מעולה! 🎊 from math import sqrt מייבא רק את sqrt ואפשר להשתמש בה ישירות ללא math.'
        }
    }
}
