import sqlite3
import os

def save_feedback(message, category):
    conn = sqlite3.connect("data/feedback.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS feedback (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            message TEXT NOT NULL,
            category TEXT NOT NULL


        )
    """)
    cursor.execute("INSERT INTO feedback (message, category) VALUES (?, ?)", (message, category))
    conn.commit()
    conn.close()

def get_all_feedbacks(category=None):
    conn = sqlite3.connect("data/feedback.db")
    cursor = conn.cursor()
    
    if category:
        category = category.lower()
        cursor.execute("SELECT id, message, category FROM feedback WHERE LOWER(category) = ?", (category,))
    else:
        cursor.execute("SELECT id, message, category FROM feedback")
    
    rows = cursor.fetchall()
    conn.close()
    
    feedbacks = []
    for row in rows:
        feedbacks.append({
            "id": row[0],
            "message": row[1],
            "category": row[2]
        })
    return feedbacks


def init_db():
    os.makedirs("data", exist_ok=True)
    conn = sqlite3.connect("data/feedback.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS feedback (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            message TEXT NOT NULL,
            category TEXT NOT NULL                       
        )
    """)
    conn.commit()
    conn.close()


def delete_all_feedbacks():
    conn = sqlite3.connect("data/feedback.db")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM feedback")
    conn.commit()
    conn.close()
