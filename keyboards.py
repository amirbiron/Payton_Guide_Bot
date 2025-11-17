# -*- coding: utf-8 -*-
"""
מקלדות אינליין לבוט
"""

from telegram import InlineKeyboardButton, InlineKeyboardMarkup

def main_menu_keyboard():
    """תפריט ראשי"""
    keyboard = [
        [InlineKeyboardButton("📚 התחל ללמוד", callback_data="start_learning")],
        [InlineKeyboardButton("📊 ההתקדמות שלי", callback_data="my_progress")],
        [InlineKeyboardButton("📖 רשימת שיעורים", callback_data="lessons_list")],
        [InlineKeyboardButton("ℹ️ עזרה", callback_data="help")]
    ]
    return InlineKeyboardMarkup(keyboard)

def lesson_menu_keyboard(lesson_number, total_lessons):
    """תפריט שיעור"""
    keyboard = []
    
    # כפתור תרגיל
    keyboard.append([InlineKeyboardButton("✍️ פתור תרגיל", callback_data=f"exercise_{lesson_number}")])
    
    # ניווט
    nav_row = []
    if lesson_number > 1:
        nav_row.append(InlineKeyboardButton("⏮️ שיעור קודם", callback_data=f"lesson_{lesson_number-1}"))
    if lesson_number < total_lessons:
        nav_row.append(InlineKeyboardButton("⏭️ שיעור הבא", callback_data=f"lesson_{lesson_number+1}"))
    
    if nav_row:
        keyboard.append(nav_row)
    
    # חזרה לתפריט
    keyboard.append([InlineKeyboardButton("🏠 תפריט ראשי", callback_data="main_menu")])
    
    return InlineKeyboardMarkup(keyboard)

def exercise_keyboard(lesson_number, options):
    """מקלדת לתרגיל עם אפשרויות"""
    keyboard = []
    
    # כפתור לכל אפשרות
    for i, option in enumerate(options):
        keyboard.append([InlineKeyboardButton(
            f"{chr(65+i)}. {option}", 
            callback_data=f"answer_{lesson_number}_{i}"
        )])
    
    # דילוג על התרגיל
    keyboard.append([InlineKeyboardButton("⏭️ דלג", callback_data=f"skip_{lesson_number}")])
    
    return InlineKeyboardMarkup(keyboard)

def continue_learning_keyboard(lesson_number, total_lessons):
    """המשך לימוד אחרי תרגיל"""
    keyboard = []
    
    if lesson_number < total_lessons:
        keyboard.append([InlineKeyboardButton("📘 שיעור הבא", callback_data=f"lesson_{lesson_number+1}")])
    else:
        keyboard.append([InlineKeyboardButton("🎉 סיימתי את כל השיעורים!", callback_data="completed_all")])
    
    keyboard.append([InlineKeyboardButton("🏠 תפריט ראשי", callback_data="main_menu")])
    
    return InlineKeyboardMarkup(keyboard)

def lessons_list_keyboard(lessons, current_page=1, items_per_page=5):
    """רשימת שיעורים עם פגינציה"""
    keyboard = []
    
    total_lessons = len(lessons)
    start_idx = (current_page - 1) * items_per_page
    end_idx = min(start_idx + items_per_page, total_lessons)
    
    # כפתורים לשיעורים
    for i in range(start_idx, end_idx):
        lesson_num = i + 1
        title = lessons[lesson_num]['title']
        keyboard.append([InlineKeyboardButton(title, callback_data=f"lesson_{lesson_num}")])
    
    # ניווט בין דפים
    nav_row = []
    total_pages = (total_lessons + items_per_page - 1) // items_per_page
    
    if current_page > 1:
        nav_row.append(InlineKeyboardButton("◀️ הקודם", callback_data=f"lessons_page_{current_page-1}"))
    
    nav_row.append(InlineKeyboardButton(f"📄 {current_page}/{total_pages}", callback_data="ignore"))
    
    if current_page < total_pages:
        nav_row.append(InlineKeyboardButton("▶️ הבא", callback_data=f"lessons_page_{current_page+1}"))
    
    if len(nav_row) > 1:  # רק אם יש יותר מדף אחד
        keyboard.append(nav_row)
    
    # חזרה לתפריט
    keyboard.append([InlineKeyboardButton("🏠 תפריט ראשי", callback_data="main_menu")])
    
    return InlineKeyboardMarkup(keyboard)

def progress_keyboard():
    """מקלדת התקדמות"""
    keyboard = [
        [InlineKeyboardButton("📚 המשך ללמוד", callback_data="start_learning")],
        [InlineKeyboardButton("📖 כל השיעורים", callback_data="lessons_list")],
        [InlineKeyboardButton("🏠 תפריט ראשי", callback_data="main_menu")]
    ]
    return InlineKeyboardMarkup(keyboard)
