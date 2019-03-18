import mysql.connector
# Create a connection object
dbServerName    = "10.224.0.57"
dbUser          = "dimadm"
dbPassword      = "B12345d"
dbName          = "employees"
charSet         = "utf8mb4"
# cusrorType      = mysql.connector.cursors.DictCursor
 
connectionObject   = mysql.connector.connect(host=dbServerName, 
											user=dbUser, 
											password=dbPassword, 
											db=dbName, 
											charset=charSet
											# cursorclass=cusrorType
)

try:
    # Create a cursor object
    cursorObject        = connectionObject.cursor()                                     
    # SQL query string
    sqlQuery            = "CREATE TABLE Employee(id int, LastName varchar(32), FirstName varchar(32), DepartmentCode int)"   
    # Execute the sqlQuery
    cursorObject.execute(sqlQuery)
    # SQL query string

    sqlQuery            = "show tables"   
    # Execute the sqlQuery
    cursorObject.execute(sqlQuery)
    #Fetch all the rows
    rows                = cursorObject.fetchall()
    for row in rows:
        print(row)
except Exception as e:
    print("Exeception occured:{}".format(e))
finally:
    connectionObject.close()