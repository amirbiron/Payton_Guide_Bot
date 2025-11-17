from pymongo import MongoClient
from config import MONGODB_URI, DB_NAME
from datetime import datetime

class Database:
    def __init__(self):
        """התחברות למסד הנתונים"""
        self.client = MongoClient(MONGODB_URI)
        self.db = self.client[DB_NAME]
        self.users = self.db['users']
        self.progress = self.db['progress']
        
    def get_user(self, user_id):
        """קבלת נתוני משתמש"""
        return self.users.find_one({'user_id': user_id})
    
    def create_user(self, user_id, username, first_name):
        """יצירת משתמש חדש"""
        user_data = {
            'user_id': user_id,
            'username': username,
            'first_name': first_name,
            'created_at': datetime.now(),
            'current_lesson': 1,
            'completed_lessons': [],
            'total_exercises_completed': 0
        }
        self.users.insert_one(user_data)
        return user_data
    
    def update_user_progress(self, user_id, lesson_number):
        """עדכון התקדמות משתמש"""
        user = self.get_user(user_id)
        if user and lesson_number not in user.get('completed_lessons', []):
            self.users.update_one(
                {'user_id': user_id},
                {
                    '$push': {'completed_lessons': lesson_number},
                    '$inc': {'total_exercises_completed': 1},
                    '$set': {'current_lesson': lesson_number + 1}
                }
            )
    
    def get_user_progress(self, user_id):
        """קבלת סטטיסטיקות התקדמות"""
        user = self.get_user(user_id)
        if user:
            return {
                'current_lesson': user.get('current_lesson', 1),
                'completed_lessons': len(user.get('completed_lessons', [])),
                'total_exercises': user.get('total_exercises_completed', 0)
            }
        return None
    
    def save_exercise_attempt(self, user_id, lesson_number, answer, is_correct):
        """שמירת ניסיון פתרון תרגיל"""
        attempt_data = {
            'user_id': user_id,
            'lesson_number': lesson_number,
            'answer': answer,
            'is_correct': is_correct,
            'timestamp': datetime.now()
        }
        self.progress.insert_one(attempt_data)

# יצירת instance גלובלי
db = Database()
