import mysql.connector
cnx = mysql.connector.connect(host= "c1hackathondb.cqgrvtxmzwpd.us-west-2.rds.amazonaws.com", user="admin" password="password", database= "mydb")

cur = cnx.cursor(dictionary=True)
## cur.execute("select * from ta")

