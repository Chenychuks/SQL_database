import sqlite3

conn = sqlite3.connect('student.db')
cursor = conn.cursor()

cursor.execute(''' CREATE TABLE student_data(
    first_name TEXT,
    last_name TEXT,
    email TEXT
)
''')

conn.commit()

students_list = [
    ('Will', 'Johnson', 'willjohnson@gmail.com'),
    ('John', 'Smith', 'johnsmith@gmail.com'),
    ('Katy', 'Brown', 'katybrown@gmail.com'),
]

cursor.executemany('INSERT INTO student_data VALUES (?,?,?)', students_list)

conn.commit()

cursor.execute('SELECT * FROM student_data')

item = cursor.fetchall()
print('FIRST NAME' + '\t\tLAST NAME' + '\t\t\tEMAIL' + '\t\t\tCOURSE')
print('----------' + '\t\t----------' + '\t\t\t-----' + '\t\t\t-------')

for item in item:
    print(item[0] + ' \t\t\t ' + item[1] +
          ' \t\t\t ' + item[2] + ' \t\t\t ' + item[3])


conn.commit()

# Renaming the student_date table table

cursor.execute('ALTER TABLE student_data RENAME TO data_scientist')
conn.commit

# Adding new column

conn.execute('ALTER TABLE data_scientist ADD COLUMN course')
conn.commit()

# Adding value to the newly created column

conn.execute(''' UPDATE data_scientist SET course = 'data_science' ''')
conn.commit()

cursor.execute('SELECT * FROM data_scientist')

item = cursor.fetchall()
print('FIRST NAME' + '\t\tLAST NAME' + '\t\t\tEMAIL' + '\t\t\tCOURSE')
print('----------' + '\t\t----------' + '\t\t\t-----' + '\t\t\t-------')

for item in item:
    print(item[0] + ' \t\t\t ' + item[1] +
          ' \t\t\t ' + item[2] + '\t\t\t' + item[3])
