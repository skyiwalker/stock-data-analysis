import pymysql

connection = pymysql.connect(host='localhost', port=3366, db='INVESTAR', 
    user='root', passwd='2tjrrms#@', autocommit=True)  

cursor = connection.cursor()
cursor.execute("SELECT VERSION();")
result = cursor.fetchone()

print ("MariaDB version : {}".format(result))

connection.close()