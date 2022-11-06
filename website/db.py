import mysql.connector
from mysql.connector import errorcode

config = {
  'user': 'root',
  'password': 'my-secret-pw',
  'host': '172.17.0.2',
  'database': 'demo',
  'raise_on_warnings': True
}

def opendb():
    try:
        cnx = mysql.connector.connect(
                user='root', password='my-secret-pw',
                host='172.17.0.2', database='demo')

    except mysql.connector.Error as err:
            
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)

    return cnx