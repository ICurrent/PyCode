import mysql.connector
import pandas as pd

db = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = '',
    database = 'sakila')

cusor = db.cursor()
cusor.execute('SELECT * FROM rental;')

a={}
for i in rcusor:
    a
print(a)
