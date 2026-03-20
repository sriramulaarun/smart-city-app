import sqlite3
import os

db_path = r"c:\Users\srira\OneDrive\Desktop\python\final\instance\database.db"
if os.path.exists(db_path):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    try:
        cursor.execute("ALTER TABLE reports ADD COLUMN upvotes INTEGER DEFAULT 0;")
        print("Column added successfully to instance db.")
    except sqlite3.OperationalError as e:
        print(f"Skipping: {e}")
    conn.commit()
    conn.close()
else:
    print("DB not found at", db_path)
