import mysql.connector as mysql

db = mysql.connect(
    host="localhost",
    user="root",
    passwd="naskevich8",
    database="orders"
)

cursor = db.cursor()

query = "SELECT ord_no, ord_date, purch_amt FROM orders WHERE salesman_id = 5002"
cursor.execute(query)
print(cursor.fetchall())

query = "SELECT DISTINCT salesman_id FROM orders"
cursor.execute(query)
print(cursor.fetchall())

query = "SELECT ord_date, salesman_id, ord_no, purch_amt FROM orders"
cursor.execute(query)
print(cursor.fetchall())

query = "SELECT customer_id FROM orders WHERE ord_no BETWEEN 70001 AND 70007"
cursor.execute(query)
print(cursor.fetchall())
