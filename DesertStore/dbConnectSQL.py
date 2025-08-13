import pymysql

class Database:

    connection = pymysql.connect(host='localhost', port=3306, user='root', password='root')
    cursor = connection.cursor()

    def createCart(self):
        self.cursor.execute("CREATE DATABASE IF NOT EXIST DesertStore")
        self.cursor.execute("USE DesertStore")
        self.cursor.execute("CREATE TABLE IF NOT EXIST Cart")

    def showCart(self):
        self.cursor.execute("SELECT * FROM Cart")
        data = self.cursor.fetchall()
        return data

    def insertToCart(self, item):
        self.cursor.e