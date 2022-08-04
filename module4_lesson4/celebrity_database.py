import sqlite3

conn = sqlite3.connect('celeb.db')
cur = conn.cursor()

cur.execute('''
            CREATE TABLE IF NOT EXISTS celeb
            (name TEXT PRIMARY KEY, genre TEXT, num_album INTEGER, age INTEGER, 
            awards INTEGER, year_in_industry INTEGER)
''')

conn.commit()

celeb_data = [
    ('Titilayo Adedokun', 'Jazz', 16, 34, 5, 7),
    ('Niyola', 'Soul', 25, 32, 7, 7),
    ('Douye', 'Jazz', 3, 25, 1, 3),
    ('Davido', 'Pop', 5, 32, 5, 9),
    ('Ayra Star', 'Soul', 8, 34, 2, 3),
    ('Olu Maintain', 'Pop', 32, 43, 6, 10),
    ('Phatiah', 'Soul', 7, 45, 8, 9),
    ('Wizkid', 'pop', 45, 36, 25, 8),
    ('Chris Ajilo', 'Highlife', 8, 43, 13, 6),
    ('2Baba', 'Rhyme and Blues', 49, 44, 34, 15),
    ('Iyanya', 'Pop', 12, 42, 8, 12),
    ('Banky W', 'Rhyme and Blues', 13, 39, 13, 12),
    ('Wandy Coal', 'Pop', 21, 38, 14, 7),
    ('Tiwa Savage', 'Rhyme and Blues', 23, 38, 21, 9),
    ('Kcee', 'Pop', 13, 42, 12, 11),
    ('Bez', 'Rock', 11, 32, 11, 5),
    ('Seyi Shay', 'Rhyme and Blues', 3, 27, 2, 3),
    ('Brymo', 'Pop', 11, 37, 7, 9),
    ('Samsong', 'Rhyme and Blues', 12, 32, 6, 9),
    ('Nonso Bassey', 'Pop', 8, 38, 3, 4),
    ('Demi Grace', 'Rhyme and Blues', 15, 44, 5, 12),
    ('Chidinma', 'Pop', 22, 34, 4, 6),
    ('Fela Sowande', 'Classic', 26, 81, 12, 50),
    ('Waje', 'Pop', 13, 32, 4, 6),
    ('Monica', 'Highlife', 15, 43, 5, 7),
    ('Timi Dakolo', 'Soul', 5, 33, 7, 6),
    ('Victor Uwaifo', 'Highlife', 9, 45, 4, 5),
    ('Asikey', 'Rock', 6, 54, 6, 8)
]
cur.executemany('INSERT INTO celeb VALUES (?,?,?,?,?,?)', celeb_data)
conn.commit()

cur.execute('SELECT * FROM celeb')

item = cur.fetchall()
print('NAME' + '\t\t\tGENRE' + '\t\t\t\tNUM_ALBUM' +
      '\t\t\tAGE' + '\t\t\tAWARD' + '\t\tYEARS_IN_INDUSTRY')
print('----------' + '\t\t--------' + '\t\t\t----------' +
      '\t\t\t------' + '\t\t------------' + '\t\t------------------')


for item in item:
    name, genre, num_album, age, award, year_in_industry = item
    print(f"{name:16}\t{genre:16}\t{num_album:16}\t{age:16}\t{award:16}\t{year_in_industry:16}")
conn.commit()
