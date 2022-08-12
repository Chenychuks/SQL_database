import sqlite3
from unicodedata import name

conn = sqlite3.connect('store.db')

cursor = conn.cursor()

# Calculate the amount the business owner invested in the procurement of the items.


def Total_item_cost(query="SELECT SUM(cost_price) FROM stationeries"):

    cursor.execute(query)
    item = cursor.fetchall()

    print(f"TOTAL_COST_OF_ITEMS\n{'-' * 25}")

    for item in item:
        Total_item_cost = item
        print(item[0])


# Calculate the average quantity of items in stock.

def Item_average_quantity(query="SELECT AVG(quantity) FROM stationeries"):

    cursor.execute(query)
    item = cursor.fetchall()

    print(f"AVERAGE_QUANTITY_OF_ITEM\n{'-' * 25}")

    for item in item:
        Average_quantity = item
        print(item[0])

# Determine the item with the most quantity in stock


def Most_quantity(query="SELECT name, item_id, MAX(quantity) FROM stationeries"):

    cursor.execute(query)
    item = cursor.fetchall()

    print('name' + '\t\titem_id' + '\t\t\tquantity')
    print('----------' + '\t----------------' + '\t-----------')

    for item in item:
        name, item_id, quantity = item
        print(f"{name:10}\t{item_id:10}\t{quantity:10}")


# Determine the item with the least quantity in stock

def Least_quantity(query="SELECT name, item_id, MIN(quantity) FROM stationeries"):

    cursor.execute(query)
    item = cursor.fetchall()

    print('name' + '\t\titem_id' + '\t\t\tquantity')
    print('----------' + '\t----------------' + '\t-----------')

    for item in item:
        name, item_id, quantity = item
        print(f"{name:10}\t{item_id:10}\t{quantity:10}")


Total_item_cost()
Item_average_quantity()
Least_quantity()
Most_quantity()
