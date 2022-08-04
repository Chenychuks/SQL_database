import sqlite3

conn = sqlite3.connect('celeb.db')

cursor = conn.cursor()

query = '''
SELECT name FROM celeb
'''

cursor.execute(query)

item = cursor.fetchmany(7)

print(item)

for item in item:
    print(item)
