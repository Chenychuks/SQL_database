import sqlite3
import csv

conn = sqlite3.connect('waec.db')

cursor = conn.cursor()

create_table = """
CREATE TABLE exam_score (
    student_id INTEGER, name TEXT, english REAL, 
    maths REAL, physics REAL, chemistry REAL, 
    geography REAL, econimcs REAL, 
    french REAL, literature REAL, agric REAL
)
"""

cursor.execute(create_table)

with open('student.csv', 'r') as opened_file:
    read_file = csv.reader(opened_file)

    next(read_file)

    cursor.executemany("""
    INSERT INTO exam_score VALUES (?,?,?,?,?,?,?,?,?,?,?)
    """, read_file)

conn.commit()

conn.close()
