import sqlite3

con = sqlite3.connect('learners.db')
cur = con.cursor()

cur.execute('''CREATE TABLE IF NOT EXISTS learners
                    (name text PRIMARY KEY, email text)''')

my_data = [('Abubakar Adisa', 'adisaabubakar@gmail.com'),
           ('Adebisi Afolabi', 'wasola.afolabi@yahoo.com'),
           ('Adedoyin Abass', 'doyinabass0@gmail.com'),
           ('Awonaike Tawakalitu', 'purpleduralumin@gmail.com'),
           ('Babajide Adesugba', 'jide_ade@hotmail.com'),
           ('Bukola Ajayi', 'bukolam.ajayi@gmail.com'),
           ('Binta Umar', 'ubinta63@yahoo.com'),
           ('Christian Uzondu', 'uzonduchristian2@gmail.com'),
           ('Cynthia Awiya', 'awiyac@yahoo.com'),
           ('Deborah Olorunnishola', 'deboraholuw,atobi247@gmail.com'),
           ('Eke Ihuoma', 'ihuomaeke28@gmail.com'),
           ('Esther Akpanowo', 'estherakpanowo@gmail.com'),
           ('Eniola Osadare', 'dorcasosadare@gmail.com'),
           ('Etariemi Louis', 'etariemilouis@gmail.com'),
           ('Faith Amure', 'amuretalodabif@gmail.com'),
           ('Ganiyat Shittu', 'ganiyatas@gmail.com'),
           ('Gideon Uko', 'ukogideon13@gmail.com'),
           ('Idowu Adesanya', 'idsworld22@yahoo.com'),
           ('Joyce Ezeonwu', 'joyceokore@gmail.com'),
           ('Kehinde Orolade', 'kehindeorolade@gmail.com'),
           ('Kafayat  Ibrahim', 'kafayatadenike10@gmail.com'),
           ('Lawrence Aneshimokha', 'anelawrence1@gmail.com'),
           ('Mariam Adeoti', 'adetutuadebola28@gmail.com'),
           ('Ogechi Njemanze', 'ogenjemz@gmail.com'),
           ('Omowunmi Awonirana', 'mowunmi11@gmail.com'),
           ('Placidus Ali', 'Placidusali@gmail.com'),
           ('Praise Emmanuel', 'praiseemmanuel9ic@gmail.com'),
           ('Prince Ekeocha', 'prince.ekeocha@gmail.com'),
           ('Rasheedat Sikiru', 'rasheedatsikiru@gmail.com'),
           ('Ramotallah Jubril', 'jubrilramotallah03@gmail.com'),
           ('Sheriiff Azeez', 'SheriffOlaitan71@gmail.com'),
           ('Stephen Ogungbile', 'stephenfunso@gmail.com'),
           ('Temitope Bamidele', 'bamideletemitope42@gmail.com'),
           ('Theresa Karamor', 'teriekarie@gmail.com'),
           ('Tina Uyateide', 'tinauyats@gmail.com'),
           ('Victoria Chukwuno', 'chukwunovictoria@gmail.com')]

my_query = "INSERT OR IGNORE INTO learners VALUES (?,?)"
cur.executemany(my_query, my_data)


cur.execute('''
SELECT * FROM learners
'''
            )

items = cur.fetchall()

print("name" + "\t\t\t email" f"{'.' * 100}")

for item in items:
    name, email = item
    print(f"{name:16}\t{email:16}")

# for row in cur.execute('''SELECT * FROM learners'''):
#     print(row)

# con.commit()
# con.close()
