import mysql.connector

config = {
    'user': 'root',
    'password': 'root',
    'host': 'db',
    'port': '3306',
    'database': 'smarttbot_crypto'
}

mydb = mysql.connector.connect(**config)
