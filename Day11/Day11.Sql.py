#create a database

import  pandas as pd
import pymysql

# Establish a connection to the database
conn = pymysql.connect(
    host='localhost',
    user='root',
    password='root',
    db='cdac', 
    charset='utf8mb4',
    cursorclass=pymysql.cursors.DictCursor
)

try:
    with conn.cursor() as cursor:
        # Execute SQL query to select data from the students table
        sql = "SELECT * FROM students"
        cursor.execute(sql)

        # Fetch all rows from the executed query
        rows = cursor.fetchall()

        # Print the results
        for row in rows:
            print(row)
        print()

        d = pd.DataFrame(rows, columns=['id', 'name', 'age'])
        print(d)
        print()

        #Find the average age of students
        print(d['age'].mean())

        #insert data into the students table to city column
        #d['city'] = 'New York'
        print(d)

        d.to_csv("emp.csv")

finally:
    conn.close()
