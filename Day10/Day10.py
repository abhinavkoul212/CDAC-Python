import pymongo

db = pymongo.MongoClient('mongodb://localhost:27017/')

print(db.list_database_names())
#
# #Show all the collections in the database employeDemo
print(db.employeDemo.list_collection_names())
# #Show all the collections in the database employeDemo

# Read Operations
print("print one", db.employeDemo.Employee.find_one())
print("print all", [i for i in db.employeDemo.Employee.find()])
#
#
# mytable=Employee("Employee")
# print(mytable)

# print(db.list_database_names())
mydb = db["employeDemo"]
x = mydb.list_collection_names()
print(x)
#
mytable=mydb["Employee"]
a = {"EmpID": "5",
  "EmpName": "a1b",
  "Empage": 256,
  "EmpDesignation": "Engineer"}
b = {"EmpID": "6",
  "EmpName": "a1b16",
  "Empage": 28,
  "EmpDesignation": "AdvancedDeveloper"}

# Insert operations
# x = mytable.insert_one(b)
print(x)

# Update operations
myquery = {"EmpID": "5"}
newvalues = {"$set": {"EmpName": "zzzz",
                      "Empage": 500,
                      "EmpDesignation": "AdvancedDeveloper"}}
# x = mytable.update_one(myquery, newvalues)

# dELETE OPERATIONS
myquery = {"EmpID": "6"}
# x = mytable.delete_one(myquery)

# Find operations using object id
myquery = {"EmpID": "5"}
x = mytable.find_one(myquery)
print(x)

#Theory of Web Application
 #Website vs Web Application
 #Website: A website is a collection of web pages that are linked together and can be accessed by visiting the homepage of the website using a browser.
 #Web Services: A web service is a software system designed to support interoperable machine-to-machine interaction over a network.
 #Client side Scripting: Client-side scripting is a type of computer programming that runs in a web browser and processes commands on the client's computer rather than the server's computer.
 #Server side Scripting: Server-side scripting is a technique used in web development which involves employing scripts on a web server which produce a response customized for each user's request to the website.
 #Web Application: A web application is a software application that runs on a remote server and is delivered to the user's device over the Internet.
 #Server: A server is a computer program or a device that provides functionality for other programs or devices, called "clients".