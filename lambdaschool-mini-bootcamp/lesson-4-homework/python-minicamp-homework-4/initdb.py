import sqlite3

connection = sqlite3.connect('database.db')
connection.execute('CREATE table movies (name TEXT, rating INTEGER)')
connection.close()
