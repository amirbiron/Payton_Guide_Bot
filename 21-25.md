# -*- coding: utf-8 -*-
"""
שיעורים נוספים - חלק 5
שיעורים 21-25 - נושאים מתקדמים
"""

LESSONS_PART5 = {
    21: {
        'title': '🌐 שיעור 21: Web Scraping - איסוף מידע מהאינטרנט',
        'content': """
בואו נלמד איך לאסוף מידע מאתרי אינטרנט! 🕷️

🎯 <b>מה זה Web Scraping?</b>
Web Scraping הוא תהליך של איסוף מידע אוטומטי מאתרי אינטרנט!

📦 <b>ספריות שנצטרך:</b>
<code>pip install requests beautifulsoup4</code>

📡 <b>בסיסי - קבלת HTML:</b>
<code>import requests
from bs4 import BeautifulSoup

url = "https://example.com"
response = requests.get(url)
html = response.text

# יצירת אובייקט BeautifulSoup:
soup = BeautifulSoup(html, 'html.parser')
print(soup.prettify())  # HTML מסודר</code>

🔍 <b>חיפוש אלמנטים:</b>
<code># לפי תג:
title = soup.find('h1')
print(title.text)

# כל האלמנטים מסוג מסוים:
paragraphs = soup.find_all('p')
for p in paragraphs:
    print(p.text)

# לפי class:
items = soup.find_all('div', class_='item')

# לפי id:
header = soup.find(id='header')</code>

🎯 <b>CSS Selectors:</b>
<code># בחירה מתקדמת:
links = soup.select('a')  # כל הלינקים
prices = soup.select('.price')  # כל האלמנטים עם class="price"
main = soup.select('#main')  # האלמנט עם id="main"

# מורכב יותר:
items = soup.select('div.product > h2')  # h2 בתוך div.product</code>

🔗 <b>חילוץ לינקים:</b>
<code>links = soup.find_all('a')
for link in links:
    href = link.get('href')
    text = link.text
    print(f"{text}: {href}")</code>

🖼️ <b>חילוץ תמונות:</b>
<code>images = soup.find_all('img')
for img in images:
    src = img.get('src')
    alt = img.get('alt', 'ללא תיאור')
    print(f"{alt}: {src}")</code>

📊 <b>חילוץ טבלאות:</b>
<code>table = soup.find('table')
rows = table.find_all('tr')

for row in rows:
    cells = row.find_all(['td', 'th'])
    data = [cell.text.strip() for cell in cells]
    print(data)</code>

💪 <b>דוגמה מעשית - גיגול חדשות:</b>
<code>import requests
from bs4 import BeautifulSoup

def scrape_headlines():
    url = "https://news.ycombinator.com"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    headlines = soup.select('.titleline > a')
    
    print("📰 כותרות עדכניות:")
    for i, headline in enumerate(headlines[:10], 1):
        title = headline.text
        link = headline.get('href')
        print(f"{i}. {title}")
        print(f"   🔗 {link}\n")

scrape_headlines()</code>

🔄 <b>Scraping עם עיכובים (נימוס!):</b>
<code>import time
import requests
from bs4 import BeautifulSoup

urls = [
    "https://example.com/page1",
    "https://example.com/page2",
    "https://example.com/page3"
]

for url in urls:
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # עבד עם הנתונים...
    
    # המתן 2 שניות בין בקשות:
    time.sleep(2)  # כדי לא להעמיס על השרת!</code>

⚡ <b>טיפול בשגיאות:</b>
<code>def safe_scrape(url):
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        
        soup = BeautifulSoup(response.text, 'html.parser')
        return soup
        
    except requests.exceptions.RequestException as e:
        print(f"שגיאה: {e}")
        return None

soup = safe_scrape("https://example.com")
if soup:
    # עבוד עם הנתונים...</code>

🎨 <b>Headers - להראות כמו דפדפן:</b>
<code>headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
}

response = requests.get(url, headers=headers)</code>

💾 <b>שמירת נתונים ל-CSV:</b>
<code>import csv

data = []  # נתונים שאספנו

with open('results.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(['כותרת', 'מחיר', 'קישור'])  # כותרות
    writer.writerows(data)</code>

⚠️ <b>חוקי Web Scraping:</b>
• בדוק את robots.txt של האתר
• אל תעמיס על השרת (שימוש ב-delays)
• כבד את תנאי השימוש
• אל תשתמש בנתונים לרעה
• שקול להשתמש ב-API אם קיים

🎯 <b>דוגמה מלאה - גרפי מחירים:</b>
<code>import requests
from bs4 import BeautifulSoup
import time

def scrape_products(url):
    products = []
    
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
        }
        
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # חילוץ מוצרים (דוגמה):
        items = soup.select('.product-item')
        
        for item in items:
            name = item.select_one('.product-name')
            price = item.select_one('.product-price')
            
            if name and price:
                products.append({
                    'name': name.text.strip(),
                    'price': price.text.strip()
                })
        
        return products
        
    except Exception as e:
        print(f"שגיאה: {e}")
        return []

# שימוש:
products = scrape_products("https://example.com/products")
for product in products:
    print(f"{product['name']}: {product['price']}")</code>

📚 <b>ספריות נוספות:</b>
• <b>Selenium:</b> לאתרים דינמיים (JavaScript)
• <b>Scrapy:</b> framework מקצועי ל-scraping
• <b>lxml:</b> מהיר יותר מ-BeautifulSoup
• <b>Playwright:</b> חלופה מודרנית ל-Selenium

💡 <b>טיפים חשובים:</b>
• תמיד בדוק את תנאי השימוש של האתר
• שמור על delays סבירים בין בקשות
• שקול אם יש API - זה יותר טוב!
• שמור את הנתונים לפני עיבוד נוסף
• טפל טוב בשגיאות
""",
        'exercise': {
            'question': 'איזו ספרייה משמשת לפירוש HTML ב-Python?',
            'options': ['requests', 'BeautifulSoup', 'json', 'urllib'],
            'correct_answer': 'BeautifulSoup',
            'explanation': 'נכון! 🎯 BeautifulSoup משמשת לפירוש וניתוח HTML, בעוד requests משמש להורדת העמודים'
        }
    },
    
    22: {
        'title': '🔐 שיעור 22: עבודה עם Regex - ביטויים רגולריים',
        'content': """
בואו נלמד כלי עוצמתי לעבודה עם טקסט! 🔍

🎯 <b>מה זה Regex?</b>
Regular Expressions (ביטויים רגולריים) הם דרך לחיפוש ועיבוד דפוסים בטקסט!

📦 <b>הספרייה re:</b>
<code>import re

# חיפוש פשוט:
text = "אני אוהב Python וגם JavaScript"
result = re.search("Python", text)
if result:
    print("נמצא!")  # נמצא!</code>

🔍 <b>פונקציות בסיסיות:</b>
<code># search - מציאה ראשונה:
result = re.search(r'\d+', 'יש לי 25 שקלים')
print(result.group())  # 25

# findall - כל ההתאמות:
numbers = re.findall(r'\d+', 'יש לי 25 שקלים ו-30 אגורות')
print(numbers)  # ['25', '30']

# match - התאמה מתחילת המחרוזת:
result = re.match(r'Hello', 'Hello World')

# sub - החלפה:
new_text = re.sub(r'\d+', 'XXX', 'יש לי 25 שקלים')
print(new_text)  # יש לי XXX שקלים</code>

🎨 <b>דפוסים בסיסיים:</b>
<code># נקודה (.) - כל תו:
re.findall(r'a.c', 'abc adc a1c')  # ['abc', 'adc', 'a1c']

# כוכבית (*) - 0 או יותר:
re.findall(r'ab*c', 'ac abc abbc')  # ['ac', 'abc', 'abbc']

# פלוס (+) - 1 או יותר:
re.findall(r'ab+c', 'ac abc abbc')  # ['abc', 'abbc']

# סימן שאלה (?) - 0 או 1:
re.findall(r'ab?c', 'ac abc abbc')  # ['ac', 'abc']</code>

🔢 <b>מספרים וספרות:</b>
<code># \d - ספרה (0-9):
re.findall(r'\d', 'יש לי 25 שקלים')  # ['2', '5']
re.findall(r'\d+', 'יש לי 25 שקלים')  # ['25']

# \D - לא ספרה:
re.findall(r'\D+', 'abc123def')  # ['abc', 'def']

# טווח של מספרים:
re.findall(r'\d{2,4}', 'יש 5 או 25 או 250')  # ['25', '250']</code>

🔤 <b>אותיות ומילים:</b>
<code># \w - אות, ספרה או _:
re.findall(r'\w+', 'Hello World 123')  # ['Hello', 'World', '123']

# \W - לא אות/ספרה:
re.findall(r'\W+', 'Hello, World!')  # [', ', '!']

# \s - רווח:
re.findall(r'\w+\s\w+', 'Hello World')  # ['Hello World']

# \S - לא רווח:
re.findall(r'\S+', 'Hello World')  # ['Hello', 'World']</code>

📍 <b>עוגנים (Anchors):</b>
<code># ^ - תחילת מחרוזת:
re.match(r'^Hello', 'Hello World')  # מתאים
re.match(r'^World', 'Hello World')  # לא מתאים

# $ - סוף מחרוזת:
re.search(r'World$', 'Hello World')  # מתאים
re.search(r'Hello$', 'Hello World')  # לא מתאים

# \b - גבול מילה:
re.findall(r'\bPython\b', 'Python is Pythonic')  # ['Python']</code>

📦 <b>קבוצות (Groups):</b>
<code># סוגריים () ליצירת קבוצה:
text = "אני בן 25 ונולדתי ב-1998"
result = re.search(r'בן (\d+)', text)
print(result.group(1))  # 25

# קבוצות מרובות:
result = re.search(r'בן (\d+) ונולדתי ב-(\d+)', text)
print(result.group(1))  # 25
print(result.group(2))  # 1998

# קבוצות עם שמות:
result = re.search(r'בן (?P<age>\d+)', text)
print(result.group('age'))  # 25</code>

🎯 <b>Classes - סטים של תווים:</b>
<code># סוגריים מרובעים []:
re.findall(r'[aeiou]', 'hello')  # ['e', 'o']

# טווח:
re.findall(r'[a-z]', 'Hello123')  # ['e', 'l', 'l', 'o']
re.findall(r'[0-9]', 'Hello123')  # ['1', '2', '3']

# שלילה (^):
re.findall(r'[^0-9]+', 'abc123def')  # ['abc', 'def']</code>

✉️ <b>ולידציה של אימייל:</b>
<code>def validate_email(email):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return bool(re.match(pattern, email))

print(validate_email("user@example.com"))  # True
print(validate_email("invalid.email"))      # False</code>

📱 <b>ולידציה של טלפון:</b>
<code>def validate_phone(phone):
    # פורמט: 050-1234567 או 0501234567
    pattern = r'^05\d{1}-?\d{7}$'
    return bool(re.match(pattern, phone))

print(validate_phone("050-1234567"))  # True
print(validate_phone("0501234567"))   # True
print(validate_phone("123456"))       # False</code>

🔗 <b>חילוץ URLs:</b>
<code>text = "בקר באתר https://www.example.com או http://test.co.il"
urls = re.findall(r'https?://[^\s]+', text)
print(urls)  # ['https://www.example.com', 'http://test.co.il']</code>

💰 <b>חילוץ מחירים:</b>
<code>text = "המוצר עולה 99.90₪ או $50"
prices = re.findall(r'\d+\.?\d*[₪$]', text)
print(prices)  # ['99.90₪', '50$']</code>

🎨 <b>ניקוי טקסט:</b>
<code># הסרת תגי HTML:
html = "<p>Hello <b>World</b>!</p>"
clean = re.sub(r'<[^>]+>', '', html)
print(clean)  # Hello World!

# הסרת רווחים מיותרים:
text = "Hello    World   !"
clean = re.sub(r'\s+', ' ', text).strip()
print(clean)  # Hello World !</code>

📝 <b>פיצול מתקדם:</b>
<code># split עם regex:
text = "תפוח,בננה;אבטיח:תפוז"
fruits = re.split(r'[,;:]', text)
print(fruits)  # ['תפוח', 'בננה', 'אבטיח', 'תפוז']</code>

💪 <b>דוגמה מקיפה - ניתוח לוג:</b>
<code>import re

log = """
2024-01-15 10:30:45 ERROR Connection failed
2024-01-15 10:31:12 INFO User logged in
2024-01-15 10:35:20 ERROR Database timeout
"""

# חילוץ שגיאות:
errors = re.findall(r'(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}) ERROR (.+)', log)

for timestamp, message in errors:
    print(f"{timestamp}: {message}")</code>

🔥 <b>Flags - אפשרויות נוספות:</b>
<code># re.IGNORECASE - התעלם מגודל אותיות:
result = re.findall(r'python', 'Python PYTHON python', re.IGNORECASE)
# ['Python', 'PYTHON', 'python']

# re.MULTILINE - ^ ו-$ לכל שורה:
text = "שורה 1\nשורה 2"
result = re.findall(r'^שורה', text, re.MULTILINE)
# ['שורה', 'שורה']

# re.DOTALL - . כולל \n:
text = "שורה 1\nשורה 2"
result = re.search(r'.+', text, re.DOTALL)

# שילוב flags:
result = re.findall(r'python', text, re.IGNORECASE | re.MULTILINE)</code>

⚡ <b>compile - ביצועים טובים יותר:</b>
<code># אם משתמשים באותו pattern הרבה פעמים:
pattern = re.compile(r'\d+')

numbers1 = pattern.findall('יש 25 שקלים')
numbers2 = pattern.findall('ו-30 אגורות')</code>

📚 <b>טיפים חשובים:</b>
• השתמש ב-raw strings (r'...') ל-regex
• בדוק את ה-patterns שלך ב-regex101.com
• התחל פשוט ובנה בהדרגה
• Regex לא תמיד הפתרון הטוב ביותר
• תיעד regex מסובכים עם הערות
""",
        'exercise': {
            'question': 'איזה pattern מתאים למספר טלפון בפורמט 05X-XXXXXXX?',
            'options': [r'05\d-\d{7}', r'^05\d-\d{7}$', r'05[0-9]-[0-9]{7}', r'^05\d{1}-\d{7}$'],
            'correct_answer': r'^05\d{1}-\d{7}$',
            'explanation': 'מצוין! 🎯 ^ ו-$ מוודאים שזה כל המחרוזת, \d{1} זו ספרה אחת, ו-\d{7} זה 7 ספרות'
        }
    },
    
    23: {
        'title': '⚡ שיעור 23: Async/Await - תכנות אסינכרוני',
        'content': """
בואו נלמד איך לכתוב קוד שיכול לעשות כמה דברים בבת אחת! ⚡

🎯 <b>מה זה תכנות אסינכרוני?</b>
במקום לחכות לפעולה איטית (כמו קריאה לשרת), המשך לעשות דברים אחרים!

🔄 <b>סינכרוני vs אסינכרוני:</b>
<code># סינכרוני (רגיל):
import time

def task1():
    print("משימה 1 מתחילה")
    time.sleep(2)
    print("משימה 1 נגמרת")

def task2():
    print("משימה 2 מתחילה")
    time.sleep(2)
    print("משימה 2 נגמרת")

task1()  # מחכה 2 שניות
task2()  # מחכה עוד 2 שניות
# סה"כ: 4 שניות!</code>

⚡ <b>אסינכרוני עם async/await:</b>
<code>import asyncio

async def task1():
    print("משימה 1 מתחילה")
    await asyncio.sleep(2)
    print("משימה 1 נגמרת")

async def task2():
    print("משימה 2 מתחילה")
    await asyncio.sleep(2)
    print("משימה 2 נגמרת")

async def main():
    await asyncio.gather(task1(), task2())

asyncio.run(main())
# סה"כ: 2 שניות בלבד! שתיהן רצות ביחד</code>

📝 <b>יסודות async/await:</b>
<code># פונקציה אסינכרונית:
async def my_function():
    return "Hello"

# קריאה לפונקציה אסינכרונית:
result = await my_function()

# הרצת פונקציה אסינכרונית:
asyncio.run(my_function())</code>

💡 <b>כללים חשובים:</b>
• async def - מגדיר פונקציה אסינכרונית
• await - מחכה לפונקציה אסינכרונית (רק בתוך async def)
• asyncio.run() - מריץ פונקציה אסינכרונית

🌐 <b>דוגמה - הורדת כמה אתרים:</b>
<code>import asyncio
import aiohttp  # pip install aiohttp

async def fetch_url(session, url):
    async with session.get(url) as response:
        return await response.text()

async def main():
    urls = [
        'https://api.github.com',
        'https://api.github.com/users/octocat',
        'https://api.github.com/repos/python/cpython'
    ]
    
    async with aiohttp.ClientSession() as session:
        tasks = [fetch_url(session, url) for url in urls]
        results = await asyncio.gather(*tasks)
        
        for i, result in enumerate(results):
            print(f"URL {i+1}: {len(result)} תווים")

asyncio.run(main())
# הכל רץ במקביל! 🚀</code>

⏱️ <b>asyncio.sleep:</b>
<code>import asyncio

async def countdown(name, seconds):
    print(f"{name} מתחיל ספירה לאחור...")
    for i in range(seconds, 0, -1):
        print(f"{name}: {i}")
        await asyncio.sleep(1)
    print(f"{name} סיים!")

async def main():
    await asyncio.gather(
        countdown("Timer 1", 3),
        countdown("Timer 2", 5)
    )

asyncio.run(main())</code>

🎯 <b>asyncio.gather - הרצת כמה משימות:</b>
<code>async def task_a():
    await asyncio.sleep(1)
    return "A"

async def task_b():
    await asyncio.sleep(2)
    return "B"

async def task_c():
    await asyncio.sleep(1.5)
    return "C"

async def main():
    # כל המשימות ביחד:
    results = await asyncio.gather(task_a(), task_b(), task_c())
    print(results)  # ['A', 'B', 'C']

asyncio.run(main())</code>

🔥 <b>asyncio.create_task - משימות ברקע:</b>
<code>async def background_task():
    print("משימת רקע מתחילה")
    await asyncio.sleep(3)
    print("משימת רקע נגמרת")
    return "Done"

async def main():
    # יצירת משימה שרצה ברקע:
    task = asyncio.create_task(background_task())
    
    print("עושה משהו אחר...")
    await asyncio.sleep(1)
    print("עדיין עושה משהו...")
    
    # מחכה למשימת הרקע:
    result = await task
    print(f"תוצאה: {result}")

asyncio.run(main())</code>

⚠️ <b>טיפול בשגיאות:</b>
<code>async def risky_task():
    await asyncio.sleep(1)
    raise ValueError("משהו השתבש!")

async def safe_task():
    await asyncio.sleep(1)
    return "הצלחה"

async def main():
    tasks = [risky_task(), safe_task()]
    
    # return_exceptions=True - לא תעצור את כל המשימות:
    results = await asyncio.gather(*tasks, return_exceptions=True)
    
    for i, result in enumerate(results):
        if isinstance(result, Exception):
            print(f"משימה {i+1}: שגיאה - {result}")
        else:
            print(f"משימה {i+1}: {result}")

asyncio.run(main())</code>

⏰ <b>Timeout - הגבלת זמן:</b>
<code>async def slow_operation():
    await asyncio.sleep(10)
    return "סיימתי"

async def main():
    try:
        # מקסימום 3 שניות:
        result = await asyncio.wait_for(slow_operation(), timeout=3.0)
        print(result)
    except asyncio.TimeoutError:
        print("הפעולה לקחה יותר מדי זמן!")

asyncio.run(main())</code>

🔄 <b>asyncio.Queue - תור אסינכרוני:</b>
<code>async def producer(queue, n):
    for i in range(n):
        await asyncio.sleep(0.5)
        await queue.put(f"פריט {i}")
        print(f"הוספתי פריט {i}")

async def consumer(queue):
    while True:
        item = await queue.get()
        print(f"עיבדתי: {item}")
        await asyncio.sleep(1)
        queue.task_done()

async def main():
    queue = asyncio.Queue()
    
    # יצירת producer ו-consumer:
    producer_task = asyncio.create_task(producer(queue, 5))
    consumer_task = asyncio.create_task(consumer(queue))
    
    # מחכה ל-producer:
    await producer_task
    # מחכה שהתור יתרוקן:
    await queue.join()
    
    # עוצר את ה-consumer:
    consumer_task.cancel()

asyncio.run(main())</code>

💪 <b>דוגמה מקיפה - מערכת הודעות:</b>
<code>import asyncio
import random

async def send_message(user_id, message):
    delay = random.uniform(0.5, 2)
    await asyncio.sleep(delay)
    return f"נשלח למשתמש {user_id}: {message}"

async def send_to_many(users, message):
    tasks = [send_message(user_id, message) for user_id in users]
    results = await asyncio.gather(*tasks)
    return results

async def main():
    users = [101, 102, 103, 104, 105]
    message = "שלום! יש לך הודעה חדשה 📧"
    
    print("שולח הודעות...")
    start = asyncio.get_event_loop().time()
    
    results = await send_to_many(users, message)
    
    end = asyncio.get_event_loop().time()
    
    for result in results:
        print(result)
    
    print(f"\nזמן כולל: {end - start:.2f} שניות")

asyncio.run(main())</code>

🎨 <b>מתי להשתמש ב-async/await?</b>
✅ **כן:**
• קריאות רשת (HTTP requests)
• קריאה/כתיבה לקבצים (עם aiofiles)
• פעולות I/O
• ממתין למשתמש
• מספר משימות במקביל

❌ **לא:**
• חישובים כבדים (CPU-bound)
• פעולות מהירות
• קוד פשוט שלא צריך זאת

📚 <b>ספריות אסינכרוניות פופולריות:</b>
• <b>aiohttp:</b> HTTP client/server
• <b>aiofiles:</b> קבצים אסינכרוניים
• <b>asyncpg:</b> PostgreSQL אסינכרוני
• <b>aiomysql:</b> MySQL אסינכרוני
• <b>python-telegram-bot:</b> תומך async!

💡 <b>טיפים חשובים:</b>
• await רק בתוך async def
• השתמש ב-asyncio.gather למשימות מרובות
• טפל בשגיאות עם try/except
• שימו לב ל-deadlocks (המתנות הדדיות)
• לא מהיר יותר ל-CPU bound!
""",
        'exercise': {
            'question': 'מה המילה השמורה לקריאה לפונקציה אסינכרונית?',
            'options': ['wait', 'await', 'async', 'sleep'],
            'correct_answer': 'await',
            'explanation': 'נכון! 🎯 await משמש לקריאה לפונקציה אסינכרונית ולהמתנה לתוצאתה, ניתן להשתמש בו רק בתוך async def'
        }
    },
    
    24: {
        'title': '🧪 שיעור 24: Testing - בדיקות אוטומטיות',
        'content': """
בואו נלמד איך לוודא שהקוד שלנו עובד! 🧪

🎯 <b>למה צריך בדיקות?</b>
• לוודא שהקוד עובד כמו שצריך
• למנוע באגים
• לאפשר שינויים בביטחון
• תיעוד איך הקוד צריך לעבוד

📦 <b>unittest - ספריה מובנית:</b>
<code>import unittest

def add(a, b):
    return a + b

class TestMath(unittest.TestCase):
    def test_add_positive(self):
        self.assertEqual(add(2, 3), 5)
    
    def test_add_negative(self):
        self.assertEqual(add(-1, -1), -2)
    
    def test_add_zero(self):
        self.assertEqual(add(0, 5), 5)

if __name__ == '__main__':
    unittest.main()</code>

✅ <b>Assertions נפוצות:</b>
<code>class TestAssertions(unittest.TestCase):
    def test_equality(self):
        self.assertEqual(1 + 1, 2)
        self.assertNotEqual(1, 2)
    
    def test_boolean(self):
        self.assertTrue(True)
        self.assertFalse(False)
    
    def test_none(self):
        self.assertIsNone(None)
        self.assertIsNotNone("text")
    
    def test_in(self):
        self.assertIn(3, [1, 2, 3])
        self.assertNotIn(4, [1, 2, 3])
    
    def test_exceptions(self):
        with self.assertRaises(ValueError):
            int("abc")</code>

🎨 <b>setUp ו-tearDown:</b>
<code>class TestDatabase(unittest.TestCase):
    def setUp(self):
        """רץ לפני כל בדיקה"""
        self.connection = create_connection()
        print("התחברתי למסד נתונים")
    
    def tearDown(self):
        """רץ אחרי כל בדיקה"""
        self.connection.close()
        print("סגרתי את החיבור")
    
    def test_insert(self):
        result = self.connection.insert("test")
        self.assertTrue(result)
    
    def test_query(self):
        data = self.connection.query("SELECT * FROM test")
        self.assertIsNotNone(data)</code>

⚡ <b>pytest - הספרייה הפופולרית:</b>
<code># pip install pytest

def add(a, b):
    return a + b

# קובץ: test_math.py
def test_add():
    assert add(2, 3) == 5

def test_add_negative():
    assert add(-1, -1) == -2

def test_add_strings():
    assert add("Hello ", "World") == "Hello World"

# הרצה: pytest test_math.py</code>

🔥 <b>pytest fixtures:</b>
<code>import pytest

@pytest.fixture
def sample_data():
    """נתוני בדיקה"""
    return [1, 2, 3, 4, 5]

def test_sum(sample_data):
    assert sum(sample_data) == 15

def test_max(sample_data):
    assert max(sample_data) == 5

@pytest.fixture
def user():
    return {
        "name": "אמיר",
        "age": 25,
        "email": "amir@example.com"
    }

def test_user_name(user):
    assert user["name"] == "אמיר"</code>

💪 <b>בדיקות לחריגות:</b>
<code>import pytest

def divide(a, b):
    if b == 0:
        raise ValueError("לא ניתן לחלק באפס")
    return a / b

def test_divide_by_zero():
    with pytest.raises(ValueError):
        divide(10, 0)

def test_divide_normal():
    assert divide(10, 2) == 5</code>

🎯 <b>Parametrize - בדיקות מרובות:</b>
<code>import pytest

@pytest.mark.parametrize("input,expected", [
    (2, 4),
    (3, 9),
    (4, 16),
    (5, 25),
])
def test_square(input, expected):
    assert input ** 2 == expected

@pytest.mark.parametrize("a,b,expected", [
    (1, 2, 3),
    (10, 5, 15),
    (-1, 1, 0),
    (0, 0, 0),
])
def test_add(a, b, expected):
    assert a + b == expected</code>

📊 <b>Coverage - כיסוי קוד:</b>
<code># pip install pytest-cov

# הרצה עם coverage:
# pytest --cov=mymodule tests/

# דוח HTML:
# pytest --cov=mymodule --cov-report=html tests/</code>

🎨 <b>Mock - חיקוי אובייקטים:</b>
<code>from unittest.mock import Mock, patch
import requests

def get_user_data(user_id):
    response = requests.get(f"https://api.example.com/users/{user_id}")
    return response.json()

def test_get_user_data():
    # חיקוי של requests.get:
    with patch('requests.get') as mock_get:
        mock_get.return_value.json.return_value = {
            "id": 1,
            "name": "אמיר"
        }
        
        result = get_user_data(1)
        
        assert result["name"] == "אמיר"
        mock_get.assert_called_once_with("https://api.example.com/users/1")</code>

🔧 <b>בדיקת פונקציות עם side effects:</b>
<code>from unittest.mock import Mock, patch

class EmailSender:
    def send(self, to, subject, body):
        # קוד שולח אימייל אמיתי...
        pass

def test_email_sending():
    sender = EmailSender()
    sender.send = Mock()
    
    # משתמשים בפונקציה:
    sender.send("user@example.com", "Test", "Hello")
    
    # בודקים שנקראה:
    sender.send.assert_called_once_with(
        "user@example.com",
        "Test",
        "Hello"
    )</code>

💾 <b>בדיקות למסדי נתונים:</b>
<code>import pytest

@pytest.fixture
def db_connection():
    # חיבור לבדיקות:
    conn = connect_to_test_db()
    
    # הכנת נתונים:
    conn.execute("CREATE TABLE users (id INT, name TEXT)")
    
    yield conn  # מעביר את החיבור לבדיקה
    
    # ניקוי:
    conn.execute("DROP TABLE users")
    conn.close()

def test_insert_user(db_connection):
    db_connection.execute("INSERT INTO users VALUES (1, 'אמיר')")
    result = db_connection.execute("SELECT * FROM users WHERE id=1")
    assert result[0]['name'] == 'אמיר'</code>

🎯 <b>TDD - Test Driven Development:</b>
<code># 1. כתוב בדיקה (נכשלת):
def test_calculate_discount():
    assert calculate_discount(100, 10) == 90

# 2. כתוב קוד מינימלי:
def calculate_discount(price, discount_percent):
    return price - (price * discount_percent / 100)

# 3. הרץ בדיקה (מצליחה):
# pytest

# 4. שפר את הקוד (refactor):
def calculate_discount(price, discount_percent):
    if discount_percent < 0 or discount_percent > 100:
        raise ValueError("אחוז הנחה לא תקין")
    return price * (1 - discount_percent / 100)</code>

🔥 <b>דוגמה מקיפה - בדיקות לפונקציה מורכבת:</b>
<code>import pytest

class ShoppingCart:
    def __init__(self):
        self.items = []
    
    def add_item(self, name, price, quantity=1):
        self.items.append({
            "name": name,
            "price": price,
            "quantity": quantity
        })
    
    def get_total(self):
        return sum(item["price"] * item["quantity"] for item in self.items)
    
    def apply_discount(self, percent):
        if percent < 0 or percent > 100:
            raise ValueError("אחוז הנחה לא תקין")
        total = self.get_total()
        return total * (1 - percent / 100)

# בדיקות:
class TestShoppingCart:
    @pytest.fixture
    def cart(self):
        return ShoppingCart()
    
    def test_empty_cart(self, cart):
        assert cart.get_total() == 0
    
    def test_add_single_item(self, cart):
        cart.add_item("תפוח", 5)
        assert cart.get_total() == 5
    
    def test_add_multiple_items(self, cart):
        cart.add_item("תפוח", 5, 3)
        cart.add_item("בננה", 3, 2)
        assert cart.get_total() == 21
    
    def test_apply_discount(self, cart):
        cart.add_item("תפוח", 100)
        assert cart.apply_discount(10) == 90
    
    def test_invalid_discount(self, cart):
        cart.add_item("תפוח", 100)
        with pytest.raises(ValueError):
            cart.apply_discount(-10)
        with pytest.raises(ValueError):
            cart.apply_discount(150)</code>

📚 <b>Best Practices:</b>
• כתוב בדיקות לקוד חדש
• בדיקה אחת בודקת דבר אחד
• שמות ברורים לבדיקות
• השתמש ב-fixtures לנתוני בדיקה
• בדוק גם מקרי קצה
• הרץ בדיקות לפני commit

⚡ <b>הרצת בדיקות:</b>
<code># unittest:
python -m unittest test_module.py
python -m unittest discover

# pytest:
pytest
pytest test_module.py
pytest -v  # verbose
pytest -x  # עצור באשל ראשונה
pytest -k "test_add"  # רק בדיקות עם "test_add" בשם</code>

💡 <b>טיפים חשובים:</b>
• בדיקות הן חלק מהקוד - תתחזק אותן!
• בדיקות איטיות = בעיה
• אל תבדוק implementation details
• בדוק behavior, לא code
• השתמש ב-CI/CD להרצת בדיקות אוטומטית
""",
        'exercise': {
            'question': 'איזו פקודה מריצה בדיקות עם pytest?',
            'options': ['python test.py', 'pytest', 'unittest run', 'test --run'],
            'correct_answer': 'pytest',
            'explanation': 'נכון! 🎯 הפקודה pytest מריצה את כל הבדיקות בתיקייה. אפשר גם pytest test_file.py לקובץ ספציפי'
        }
    },
    
    25: {
        'title': '🎓 שיעור 25: Type Hints ו-Clean Code',
        'content': """
בואו נלמד איך לכתוב קוד נקי ומקצועי! ✨

🎯 <b>Type Hints - מה זה?</b>
Type Hints מאפשרים לנו לציין איזה סוג משתנים/פרמטרים/החזרות!

📝 <b>Type Hints בסיסיים:</b>
<code>def greet(name: str) -> str:
    return f"שלום {name}"

age: int = 25
price: float = 99.99
is_active: bool = True
items: list = [1, 2, 3]</code>

💡 <b>למה זה חשוב?</b>
• עוזר ל-IDE לתת suggestions
• תופס שגיאות לפני הרצה
• תיעוד טוב יותר
• קוד יותר קריא

🎨 <b>Types מורכבים:</b>
<code>from typing import List, Dict, Tuple, Optional, Union

# רשימה של מספרים שלמים:
numbers: List[int] = [1, 2, 3]

# מילון מ-string ל-int:
scores: Dict[str, int] = {"אמיר": 95, "דני": 87}

# Tuple עם טיפוסים ספציפיים:
person: Tuple[str, int] = ("אמיר", 25)

# Optional - יכול להיות None:
name: Optional[str] = None
# זה שווה ל:
name: Union[str, None] = None

# Union - כמה אפשרויות:
value: Union[int, str] = 42
value = "text"  # גם בסדר!</code>

🔧 <b>פונקציות עם Type Hints:</b>
<code>from typing import List, Dict, Optional

def calculate_average(numbers: List[float]) -> float:
    """מחשב ממוצע של רשימת מספרים"""
    return sum(numbers) / len(numbers)

def find_user(user_id: int) -> Optional[Dict[str, str]]:
    """מחזיר משתמש או None אם לא נמצא"""
    users = {
        1: {"name": "אמיר", "email": "amir@example.com"},
        2: {"name": "דני", "email": "danny@example.com"}
    }
    return users.get(user_id)

def process_data(
    data: List[int],
    multiplier: float = 1.0,
    round_result: bool = False
) -> List[float]:
    """מעבד נתונים עם אפשרויות"""
    result = [x * multiplier for x in data]
    if round_result:
        result = [round(x) for x in result]
    return result</code>

🎯 <b>Classes עם Type Hints:</b>
<code>from typing import List, Optional
from dataclasses import dataclass

@dataclass
class Person:
    name: str
    age: int
    email: Optional[str] = None
    hobbies: List[str] = None
    
    def __post_init__(self):
        if self.hobbies is None:
            self.hobbies = []

class ShoppingCart:
    def __init__(self) -> None:
        self.items: List[str] = []
        self.total: float = 0.0
    
    def add_item(self, item: str, price: float) -> None:
        self.items.append(item)
        self.total += price
    
    def get_total(self) -> float:
        return self.total</code>

🔥 <b>Generic Types:</b>
<code>from typing import TypeVar, Generic, List

T = TypeVar('T')

class Stack(Generic[T]):
    def __init__(self) -> None:
        self.items: List[T] = []
    
    def push(self, item: T) -> None:
        self.items.append(item)
    
    def pop(self) -> T:
        return self.items.pop()
    
    def is_empty(self) -> bool:
        return len(self.items) == 0

# שימוש:
int_stack: Stack[int] = Stack()
int_stack.push(1)
int_stack.push(2)

str_stack: Stack[str] = Stack()
str_stack.push("hello")
str_stack.push("world")</code>

---

✨ <b>Clean Code - קוד נקי</b>

📚 <b>שמות משתנים טובים:</b>
<code># ❌ רע:
x = 5
d = {"n": "John", "a": 25}
def fn(a, b):
    return a + b

# ✅ טוב:
max_retries = 5
user_data = {"name": "John", "age": 25}
def calculate_total(price, tax):
    return price + tax</code>

🎯 <b>פונקציות קצרות וממוקדות:</b>
<code># ❌ רע - פונקציה שעושה הכל:
def process_user(user):
    # בדיקת תקינות
    if not user.get("email"):
        return False
    # שליחת אימייל
    send_email(user["email"], "Welcome")
    # שמירה במסד נתונים
    db.save(user)
    # עדכון לוג
    log.info(f"User {user['id']} processed")
    return True

# ✅ טוב - פונקציות קטנות:
def validate_user(user: Dict) -> bool:
    return bool(user.get("email"))

def send_welcome_email(email: str) -> None:
    send_email(email, "Welcome")

def save_user_to_db(user: Dict) -> None:
    db.save(user)

def log_user_processing(user_id: int) -> None:
    log.info(f"User {user_id} processed")

def process_user(user: Dict) -> bool:
    if not validate_user(user):
        return False
    
    send_welcome_email(user["email"])
    save_user_to_db(user)
    log_user_processing(user["id"])
    return True</code>

💬 <b>הערות טובות:</b>
<code># ❌ רע - הערה מיותרת:
x = x + 1  # מוסיף 1 ל-x

# ❌ רע - הערה שקרית:
# מחזיר True אם המשתמש פעיל
def check_user(user):
    return user.status == "inactive"  # באג!

# ✅ טוב - הסבר למה, לא מה:
# נשתמש בזמן קצוב כי השרת החיצוני לפעמים איטי
response = requests.get(url, timeout=10)

# ✅ טוב - הסבר לקוד מורכב:
# אלגוריתם Quick Sort - O(n log n) ממוצע
# אבל O(n²) במקרה הגרוע ביותר
def quick_sort(arr):
    # ...</code>

🎨 <b>Magic Numbers - הימנע מהם:</b>
<code># ❌ רע:
if user.age > 18:
    allow_access()

if price * 1.17 > budget:
    show_error()

# ✅ טוב:
LEGAL_AGE = 18
VAT_RATE = 1.17

if user.age > LEGAL_AGE:
    allow_access()

if price * VAT_RATE > budget:
    show_error()</code>

🔧 <b>DRY - Don't Repeat Yourself:</b>
<code># ❌ רע - קוד חוזר:
user1_full_name = user1["first_name"] + " " + user1["last_name"]
user2_full_name = user2["first_name"] + " " + user2["last_name"]
user3_full_name = user3["first_name"] + " " + user3["last_name"]

# ✅ טוב - פונקציה:
def get_full_name(user: Dict[str, str]) -> str:
    return f"{user['first_name']} {user['last_name']}"

user1_full_name = get_full_name(user1)
user2_full_name = get_full_name(user2)
user3_full_name = get_full_name(user3)</code>

⚡ <b>Early Return:</b>
<code># ❌ רע - קינון עמוק:
def process_payment(amount, user):
    if amount > 0:
        if user.is_verified:
            if user.balance >= amount:
                # עיבוד תשלום
                return True
            else:
                return False
        else:
            return False
    else:
        return False

# ✅ טוב - early returns:
def process_payment(amount: float, user: User) -> bool:
    if amount <= 0:
        return False
    
    if not user.is_verified:
        return False
    
    if user.balance < amount:
        return False
    
    # עיבוד תשלום
    return True</code>

📦 <b>ארגון קוד טוב:</b>
<code># מבנה קובץ טוב:

# 1. Imports
import os
from typing import List, Dict

# 2. קבועים
MAX_RETRIES = 3
DEFAULT_TIMEOUT = 30

# 3. Classes
class User:
    def __init__(self, name: str):
        self.name = name

# 4. פונקציות
def process_data(data: List[int]) -> List[int]:
    return [x * 2 for x in data]

# 5. Main
if __name__ == "__main__":
    main()</code>

🎯 <b>SOLID Principles (בקצרה):</b>
<code># S - Single Responsibility
# כל class עושה דבר אחד

# O - Open/Closed  
# פתוח להרחבה, סגור לשינוי

# L - Liskov Substitution
# אפשר להחליף class בתת-class שלו

# I - Interface Segregation
# ממשקים קטנים וממוקדים

# D - Dependency Inversion
# תלות בהפשטות, לא במימושים</code>

💪 <b>Code Review Checklist:</b>
<code>✅ שמות משתנים ופונקציות ברורים?
✅ פונקציות קצרות (< 50 שורות)?
✅ אין קוד חוזר?
✅ יש type hints?
✅ יש docstrings לפונקציות מורכבות?
✅ טיפול בשגיאות?
✅ יש בדיקות?
✅ הקוד קריא?</code>

🔥 <b>דוגמה מקיפה - לפני ואחרי:</b>
<code># ❌ לפני:
def p(d):
    t = 0
    for i in d:
        t += i["p"] * i["q"]
    if t > 100:
        t = t * 0.9
    return t

# ✅ אחרי:
from typing import List, Dict

def calculate_cart_total(items: List[Dict[str, float]]) -> float:
    """
    מחשב את סכום העגלה כולל הנחה לקניה מעל 100₪.
    
    Args:
        items: רשימת פריטים, כל פריט עם 'price' ו-'quantity'
    
    Returns:
        הסכום הכולל אחרי הנחה
    """
    DISCOUNT_THRESHOLD = 100
    DISCOUNT_RATE = 0.9
    
    total = sum(item["price"] * item["quantity"] for item in items)
    
    if total > DISCOUNT_THRESHOLD:
        total *= DISCOUNT_RATE
    
    return total</code>

📚 <b>ספרים מומלצים:</b>
• Clean Code - Robert C. Martin
• The Pragmatic Programmer
• Refactoring - Martin Fowler

💡 <b>זכור:</b>
"כל טיפש יכול לכתוב קוד שמחשב מבין.
מתכנתים טובים כותבים קוד שבני אדם מבינים."
- Martin Fowler
""",
        'exercise': {
            'question': 'מה הפורמט הנכון של Type Hint לפונקציה שמקבלת int ומחזירה str?',
            'options': ['def func(x) -> str:', 'def func(x: int) -> str:', 'def func(x: str) -> int:', 'def func(x): -> str'],
            'correct_answer': 'def func(x: int) -> str:',
            'explanation': 'מעולה! 🎯 הפורמט הנכון: שם פרמטר: טיפוס ואחרי הסוגריים -> טיפוס_החזרה'
        }
    }
}
