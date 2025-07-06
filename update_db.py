import sqlite3

# Connect to your existing SQLite database
conn = sqlite3.connect('database.db')  # Change this if your DB file is named differently
cursor = conn.cursor()

try:
    # Add the missing column if it doesn't exist
    cursor.execute("ALTER TABLE posts ADD COLUMN doc_path TEXT;")
    print("✅ Column 'doc_path' added successfully.")
except sqlite3.OperationalError as e:
    print("⚠️ Error:", e)

conn.commit()
conn.close()
