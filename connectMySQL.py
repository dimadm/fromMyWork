import mysql.connector

cnx = mysql.connector.connect(user = 'dimadm', password = 'B12345d',
                              host = '10.224.0.57',
                              database = 'dimadmDB')
cur = database.cursor()
cur.execute("SELECT * FROM Table01")
for row in cur.fetchall():
    print row[0]

database.close()
cnx.close()