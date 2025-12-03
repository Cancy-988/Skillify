import sqlite3

conn = sqlite3.connect("data/users.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS quiz_results (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    email TEXT,
    coding INTEGER,
    aptitude INTEGER,
    problem_solving INTEGER,
    communication INTEGER,
    confidence INTEGER,
    total_score INTEGER,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)
""")

conn.commit()
conn.close()

print("Quiz results table created successfully!")

