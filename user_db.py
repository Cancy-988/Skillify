import sqlite3

connection = sqlite3.connect("data/users.db")



cursor = connection.cursor()


cursor.execute("ALTER TABLE users ADD COLUMN role TEXT DEFAULT 'student'")
connection.commit()

cursor.execute("INSERT INTO users (name, email, password, role) VALUES (?, ?, ?, ?)", 
               ("Admin", "admin@gmail.com", "admin123", "admin"))

connection.commit()
connection.close()

print("Database and users table created successfully!")
