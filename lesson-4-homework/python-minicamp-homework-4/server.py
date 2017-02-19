from flask import Flask, render_template, request, jsonify
import sqlite3

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/movie', methods=['POST'])
def movie():
    connection = sqlite3.connect('database.db')
    cursor = connection.cursor()
    name = request.form['name']
    rating = request.form['rating']

    try:
        cursor.execute('INSERT INTO movies(name, rating) VALUES (?,?)', (name, rating))
        connection.commit()
        message = 'Success'
    except:
        connection.rollback()
        message = 'Error'
    finally:
        connection.close()
        return message

@app.route('/movies')
def movies():
    connection = sqlite3.connect('database.db')
    cursor = connection.cursor()
    cursor.execute('SELECT * from movies')
    movieList = cursor.fetchall()
    connection.close()
    return jsonify(movieList)

@app.route('/search')
def search():
    connection = sqlite3.connect('database.db')
    cursor = connection.cursor()
    name = (request.args['name'],)
    cursor.execute('SELECT * FROM movies WHERE name = ?', (name))
    movies = cursor.fetchall()
    connection.close
    if movies != []:
        return jsonify(movies)
    else:
        return 'No results'

app.run(debug = True)
