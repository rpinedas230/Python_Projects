import mysql.connector

base_de_datos = mysql.connector.connect(
    host = 'localhost', 
    user = 'root', 
    password = "", 
    database= 'pythondb',
    port = '3308'
)
