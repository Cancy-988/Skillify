import sqlite3

conn = sqlite3.connect("data/users.db")
cursor = conn.cursor()

cursor.execute("ALTER TABLE users ADD COLUMN profile_pic TEXT")
conn.commit()
conn.close()

print("Profile picture column added!")
