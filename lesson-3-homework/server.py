from flask import Flask, render_template, request, jsonify
import sqlite3
import pdb

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/enternew')
def enternew():
    return render_template('food.html')

@app.route('/addfood', methods=['POST'])
def addfood():
    connection=sqlite3.connect('database.db')
    cursor=connection.cursor()
    try:
        name=request.form['name']
        calories=request.form['calories']
        cuisine=request.form['cuisine']
        is_vegetarian=request.form['is_vegetarian']
        is_gluten_free=request.form['is_gluten_free']
        cursor.execute('INSERT INTO foods (name,calories,cuisine,is_vegetarian,is_gluten_free) VALUES (?,?,?,?,?)', (name,calories,cuisine,is_vegetarian,is_gluten_free))
        connection.commit()
        message = 'Record successfully added'
    except:
        connection.rollback()
        message = 'Error in insert operation'
    finally:
        return render_template('result.html', message=message)
        connection.close()

@app.route('/favorite')
def favorite():
    connection=sqlite3.connect('database.db')
    cursor=connection.cursor()
    cursor.execute('SELECT * from foods WHERE name = "Pesto Pasta"')
    return jsonify(cursor.fetchone())
    connection.close()

@app.route('/search')
def search():
    connection=sqlite3.connect('database.db')
    cursor=connection.cursor()
    food=(request.args['name'],)
    cursor.execute('SELECT * from foods WHERE name=?', food)
    results = jsonify(cursor.fetchall())
    if results:
        return results
    else:
        return 'No results!'
    connection.close()

@app.route('/drop')
def drop():
    connection = sqlite3.connect('database.db')
    connection.execute('DROP TABLE foods ')
    connection.commit()
    return 'Database dropped successfully'
    connection.close()
