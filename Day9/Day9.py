# import pymysql
#
# connection = pymysql.connect(host='localhost',port=3306,user='root',password='root', database='cdac')
#
# mycursor = connection.cursor()
#
# mycursor.execute("create table students(id int primary key, name varchar(20), age int)")
# # mycursor.execute("CREATE DATABASE cdac")
# mycursor.execute("insert into student values(1,'Rahul',20)")
# #
# mycursor.execute("insert into student values(2,'Rohit',21)")
# connection.commit()
#
# mycursor.close()
#
# connection.close()
import pymysql

# Connect to the database
connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', database='cdac')

try:
    mycursor = connection.cursor()

    # Create table if it does not exist
    mycursor.execute("CREATE TABLE IF NOT EXISTS students (id INT PRIMARY KEY, name VARCHAR(20), age INT)")

    # Insert data using parameterized queries
    mycursor.execute("INSERT INTO students (id, name, age) VALUES (%s, %s, %s)", (5, 'Ramesh', 20))
    mycursor.execute("INSERT INTO students (id, name, age) VALUES (%s, %s, %s)", (6, 'Rajesh', 21))

    # Commit the transaction
    connection.commit()

finally:
    # Close the cursor and connection
    mycursor.close()
    connection.close()

#ACID Properties
#A stands for Atomicity: It means that all the operations in a transaction should be completed successfully.
     #If any operation fails, the entire transaction should be rolled back.
#C stands for Consistency: It means that the database should remain in a consistent state before and after the transaction.

#JSON: JavaScript Object Notation

