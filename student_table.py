import sqlite3

conn = sqlite3.connect("data/users.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS student_details (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_email TEXT,
    branch TEXT,
    projects INTEGER,
    internships INTEGER,
    skills TEXT,
    confidence INTEGER
)
""")

conn.commit()
conn.close()

print("Student table created successfully!")
