import mysql.connector

mydb = mysql.connector.connect(
  host="10.224.0.57",
  user="dimadm",
  passwd="B12345d",
  database="dimadmDB"
)

mycursor = mydb.cursor()

sql = "INSERT INTO table01 (name, address) VALUES (%s, %s)"
val = ("John", "Highway 21")
mycursor.execute(sql, val)

mydb.commit()

print(mycursor.rowcount, "record inserted.")







mycursor.execute("SELECT * FROM table01")

myresult = mycursor.fetchall()

for x in myresult:
  print(x)
 