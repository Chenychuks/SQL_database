import sqlite3

conn = sqlite3.connect('waec.db')

cursor = conn.cursor()

# Best student in maths


def best_maths(query="SELECT student_id, name, MAX(maths) FROM exam_score"):

    cursor.execute(query)
    item = cursor.fetchall()

    print('Student_id' + '\t\tname' + '\t\tScore')
    print('----------' + '\t----------------' + '\t-----------')

    for item in item:
        student_id, name, score = item
        print(f"{student_id:10}\t{name:10}\t{score:10}")


# Least student in English

def lowest_english(query="SELECT student_id, name, MIN(english) FROM exam_score"):

    cursor.execute(query)
    item = cursor.fetchall()

    print('Student_id' + '\t\tname' + '\t\tScore')
    print('----------' + '\t--------------' + '\t\t-----------')

    for item in item:
        student_id, name, score = item
        print(f"{student_id:10}\t{name:10}\t{score:10}")

# Average score in maths


def average_maths(query="SELECT AVG(maths) AS 'average' FROM exam_score"):

    cursor.execute(query)
    item = cursor.fetchall()

    print(f"Average_score_maths\n{'-' * 25}")

    for item in item:
        Average_score = item
        print(item[0])

# Average score in English


def average_english(query="SELECT AVG(english) AS 'average' FROM exam_score"):

    cursor.execute(query)
    item = cursor.fetchall()

    print(f"Average_score_english\n{'-' * 25}")

    for item in item:
        Average_score = item
        print(item[0])


# Who is the best performing student across all nine subjects in terms of overall scores
# Method 1 : finding the maximum value from the sum accross multiple columns in sql

def max_value(query=""" SELECT name, student_id, MAX(COALESCE(maths,0) + COALESCE(physics,0) + COALESCE(chemistry,0) + COALESCE(geography,0) + 
    COALESCE(french,0) + COALESCE(econimcs,0) + COALESCE(literature,0) + 
    COALESCE(agric,0) + COALESCE(english,0)) as Total FROM exam_score 
    """):
    cursor.execute(query)
    item = cursor.fetchall()

    print('name' + '\t\t\tStudent_id' + '\t\tTotal_Score')
    print('----------------' + '\t--------------' + '\t\t-----------')

    for item in item:
        name, student_id, Total_score = item
        print(f"{name:10}\t{student_id:10}\t{Total_score:10}")


# Who is the best performing student across all nine subjects in terms of overall scores
# Method 2 : finding the maximum value from the sum accross multiple columns in sql
def maximum_value(query="""
    SELECT name, student_id, MAX(maths + english + physics + chemistry + geography + french + econimcs + literature + agric )
    FROM exam_score
    """):
    cursor.execute(query)
    item = cursor.fetchall()

    print('name' + '\t\t\tStudent_id' + '\t\tTotal_Score')
    print('----------------' + '\t--------------' + '\t\t-----------')

    for item in item:
        name, student_id, Total_score = item
        print(f"{name:10}\t{student_id:10}\t{Total_score:10}")

# Who is the best performing student across all nine subjects in term of average scores


def max_average(query="""SELECT name, student_id, MAX(maths + english + physics + chemistry + geography + french + econimcs + literature + agric )/9 AS col_ave
    FROM exam_score
    """):
    cursor.execute(query)
    item = cursor.fetchall()

    print('name' + '\t\t\tStudent_id' + '\t\tAverage_Score')
    print('----------------' + '\t--------------' + '\t\t-----------')

    for item in item:
        name, student_id, Average_score = item
        print(f"{name:10}\t{student_id:10}\t\t{Average_score:10}")


best_maths()
lowest_english()
average_maths()
average_english()
max_value()
maximum_value()
max_average()


conn.commit()
conn.close()
