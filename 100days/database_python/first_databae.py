# import mysql.connector
# #importing database
# database = mysql.connector.connect(
#     host="localhost",
#     user="root",
#     password="",

#     database = "python_3pm"
# )

# db = database.cursor()

# db.execute("SELECT * FROM student")
# result =db.fetchall()
# for x in result:
#     print(x)

import mysql.connector

database = mysql.connector.connect(
    host ="localhost",
    user='root',
    password='',

    database = "python_3pm"

)

db = database.cursor()

db.execute("SELECT * FROM student")
result =db.fetchall()
for x in result:
    print(x)



# insert in Mysql

import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "python_3pm"
)

mycursor = mydb.cursor()
sql = "INSERT INTO python_3pm(sn,name,math,physics,english,nepali,total,per,grade) VALUES ('ktm',54,45,45,45,123,75,'D')"
mycursor.execute(sql)
mydb.commit()
print(mycursor.rowcount, "record inserted.")