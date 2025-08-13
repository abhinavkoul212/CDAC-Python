import pymysql

class Database:

    def __init__(self):
        self.connection = pymysql.connect(host='localhost', port=3306, user='root', password='root')
        self.cursor = self.connection.cursor()
        self.createCart()

    def createCart(self):
        self.cursor.execute("CREATE DATABASE IF NOT EXISTS DesertStore")
        self.cursor.execute("USE DesertStore")
        self.cursor.execute("CREATE TABLE IF NOT EXISTS Cart(id INT AUTO_INCREMENT PRIMARY KEY, Name VARCHAR(100), Quantity INT, Price FLOAT)")
        print("\n Created Database")

    def showCart(self):
        self.cursor.execute("SELECT * FROM Cart")
        data = self.cursor.fetchall()
        return data

    def insertToCart(self, name,qty,price):
        self.cursor.execute("INSERT INTO Cart(Name,Quantity,Price) VALUES (%s,%s,%s)",(name,qty,price))
        self.connection.commit()
        print("\n Insertd into Cart")

    def clearCart(self):
        self.cursor.execute("DELETE FROM Cart")
        self.connection.commit()
        print("\n Clearing Cart")

    def close(self):
        self.cursor.close()
        self.connection.close()
        print("\n Connection Closed")