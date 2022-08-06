import sqlite3

conn = sqlite3.connect('celeb.db')

cursor = conn.cursor()


def Most_decorated_celeb(column='awards'):

    query = 'SELECT name, MAX(' + column + ') FROM celeb'

    cursor.execute(query)

    item = cursor.fetchall()

    print('NAME' + '\t\t\tNO_OF_AWARDS')
    print('----------' + '\t\t---------------')

   # print(f"Celebrity_name\t\t{column}\n{'-' *40}")

    for item in item:
        name, awards = item
        print(f"{name:10}\t{awards:10}")


def Oldest_celeb(column='age'):

    query = 'SELECT name, MAX(' + column + ') FROM celeb'

    cursor.execute(query)

    item = cursor.fetchall()

    print('NAME' + '\t\t\tAGE')
    print('----------' + '\t\t---------------')

   # print(f"Celebrity_name\t\t{column}\n{'-' *40}")

    for item in item:
        name, age = item
        print(f"{name:10}\t{age:10}")


def Industry_oldest_celeb(column='year_in_industry'):

    query = 'SELECT name, MAX(' + column + ') FROM celeb'

    cursor.execute(query)

    item = cursor.fetchall()

    print('NAME' + '\t\t\tYEAR_IN_INDUSTRY')
    print('----------' + '\t\t---------------')

   # print(f"Celebrity_name\t\t{column}\n{'-' *40}")

    for item in item:
        name, year_in_industry = item
        print(f"{name:10}\t{year_in_industry:10}")


def Least_album(column='num_album'):

    query = 'SELECT name, MIN(' + column + ') FROM celeb'

    cursor.execute(query)

    item = cursor.fetchall()

    print('NAME' + '\t\t\tnum_album')
    print('----------' + '\t\t---------------')

   # print(f"Celebrity_name\t\t{column}\n{'-' *40}")

    for item in item:
        name, num_album = item
        print(f"{name:10}\t{num_album:10}")


Most_decorated_celeb('AWARDS')
Oldest_celeb('AGE')
Industry_oldest_celeb('year_in_industry')
Least_album('num_album')


def most_frequent(column='genre'):

    query = f"""
    SELECT {column}
    FROM celeb
    GROUP BY 
        genre
    ORDER BY 
        COUNT({column}) DESC
    LIMIT 1;
    """

    cursor.execute(query)

    item = cursor.fetchall()

    print(f"Most_Frequent_genre\n{'-' * 30}")

    for item in item:
        print(''.join(item))


most_frequent()
