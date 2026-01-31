import sqlite3

connection = sqlite3.connect("data/users.db")



cursor = connection.cursor()


cursor.execute("ALTER TABLE users ADD COLUMN role TEXT DEFAULT 'student'")
connection.commit()


connection.commit()
connection.close()

print("Database and users table created successfully!")
