import sqlite3

contact = sqlite3.connect('dt.db')
cursor = contact.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS User(
id INTEGER PRIMARY KEY,
username TEXT NOT NULL,
email TEXT NOT NULL,
age INTEGER,
balance INTEGER NOT NULL
)
''')
cursor.execute('''
CREATE INDEX IF NOT EXISTS idx_email ON User(email)
''')

cursor.execute('DELETE FROM User WHERE id = ?', (6,))
cursor.execute('SELECT COUNT(*) FROM User')
a = (cursor.fetchall()[0][0])
cursor.execute('SELECT SUM(balance) FROM User')
b = int(cursor.fetchall()[0][0])
print(b / a)
contact.commit()
contact.close()
