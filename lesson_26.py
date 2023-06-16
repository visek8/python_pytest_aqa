import mysql.connector as mysql

# from mysql.connector import cursor

db = mysql.connect(host="localhost",
                   user="root",
                   passwd="naskevich8",
                   database="test_db_2")

cursor = db.cursor()

cursor.execute("DESC locators")
print(cursor.fetchall())

cursor.execute("INSERT INTO locators (name, type) VALUES ('//div[@id=main_table]', 'XPATH')")
db.commit()
cursor.execute("INSERT INTO locators (name, type) VALUES ('#main_button', 'CSS')")
db.commit()
print(cursor.rowcount, "record inserted")

cursor.execute("SELECT * FROM locators")
print(cursor.fetchall())
db.close()
