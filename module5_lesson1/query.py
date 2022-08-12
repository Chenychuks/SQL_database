import sqlite3

conn = sqlite3.connect('store.db')

cursor = conn.cursor()

cursor.execute("SELECT * FROM stationeries")
query = """
SELECT name, item_id,
    CASE 
        WHEN quantity < 50 THEN 'RESTOCK'
        WHEN quantity < 100 THEN 'STILL IS STOCK BUT MIGHT NEED RESTOCKING'           
        ELSE 'DO NOT RESTOCK'
    END AS status
FROM stationeries
ORDER BY cost_price;
"""

cursor.execute(query)

item = cursor.fetchall()

print('STOCK' + '\t\tSTOCK_ID' + '\t\tSTATUS')
print('----------' + '\t--------------' + '\t\t-----------')

for item in item:
    STOCK, STOCK_ID, STATUS = item
    print(f"{STOCK:10}\t{STOCK_ID:10}\t\t{STATUS:10}")

conn.commit()
conn.close()
