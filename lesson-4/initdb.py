import sqlite3

connection = sqlite3.connect('database.db')
connection.execute('CREATE table friends (name TEXT, age INTEGER)')
connection.close()
