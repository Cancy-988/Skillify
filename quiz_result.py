import sqlite3

conn = sqlite3.connect("data/users.db")
cursor = conn.cursor()


cursor.execute("DROP TABLE IF EXISTS quiz_results")


cursor.execute("""
CREATE TABLE quiz_results (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_email TEXT NOT NULL,
    category TEXT NOT NULL,
    score INTEGER NOT NULL,
    total INTEGER NOT NULL,
    taken_on TEXT NOT NULL
)
""")

conn.commit()
conn.close()

print("Quiz results table recreated successfully!")
