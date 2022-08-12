import sqlite3

conn = sqlite3.connect('store.db')

cur = conn.cursor()

cur.execute(''' 
                     CREATE TABLE IF NOT EXISTS stationeries
                     (name TEXT PRIMARY KEY, item_id TEXT, cost_price REAL, 
                     quantity INTEGER )
 ''')

conn.commit()

Stock = [('bible', 'AD12354', 4500, 14),
         ('jotter', 'BD36454', 2100, 75),
         ('pens', 'TZ53644', 340, 21),
         ('dictionary', 'PE24764', 4500, 237),
         ('novels', 'TE37643', 2100, 53),
         ('ink', 'BR192827', 34700, 2),
         ('A4 papers', 'ZE283773', 10500, 23),
         ('envelope', 'BE273632', 230, 11),
         ('file', 'RE376532', 1200, 562),
         ('ruler', 'FE92736', 3200, 42),
         ('stamp', 'YJ293873', 3525, 121),
         ('paper clip', 'FK28372', 150, 6)
         ]
cur.executemany('INSERT INTO stationeries VALUES (?,?,?,?)', Stock)
conn.commit()

cur.execute('SELECT * FROM stationeries')

item = cur.fetchall()
print('name' + '\t\t\titem_id' + '\t\t\t\tcost_price' +
      '\t\tquantity')
print('----------' + '\t\t--------' + '\t\t\t----------' +
      '\t\t------')

for item in item:
    name, item_id, cost_price, quantity = item
    print(f"{name:16}\t{item_id:16}\t{cost_price:16}\t{quantity:16}")
conn.commit()
