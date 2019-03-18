


#Not working!


from __future__ import print_function

import mysql.connector
from mysql.connector import errorcode

mydb = mysql.connector.connect(
  host="10.224.0.57",
  user="dimadm",
  passwd="B12345d",
  database="employees"
  )
 #----------------------------------------------------- 
for table_name in employee:
    table_description = employee[table_name]
    try:
        print("Creating table {}: ".format(table_name), end='')
        cursor.execute(table_description)
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
            print("already exists.")
        else:
            print(err.msg)
    else:
        print("OK")

cursor.close()
cnx.close()