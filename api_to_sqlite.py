
import requests
import sqlite3

API_URL = "https://jsonplaceholder.typicode.com/posts"

conn = sqlite3.connect("books.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS books (
    id INTEGER PRIMARY KEY,
    title TEXT,
    author TEXT,
    publication_year INTEGER
)
""")

response = requests.get(API_URL)
data = response.json()[:10]

for i, item in enumerate(data):
    cursor.execute(
        "INSERT INTO books (title, author, publication_year) VALUES (?, ?, ?)",
        (item['title'], f"Author_{i}", 2000 + i)
    )

conn.commit()

cursor.execute("SELECT * FROM books")
for row in cursor.fetchall():
    print(row)

conn.close()
