import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="Ljbc4life!",
  database="csc2020"
)

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM customer")

myresult = mycursor.fetchall()

for x in myresult:
  print(x)