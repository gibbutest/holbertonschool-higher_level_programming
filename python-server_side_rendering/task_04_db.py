from flask import Flask, render_template, request
import json
import csv
import sqlite3

app = Flask(__name__)

@app.get('/')
def home():
    return render_template('index.html')

@app.get('/about')
def about():
    return render_template('about.html')

@app.get('/contact')
def contact():
    return render_template('contact.html')

@app.get('/items')
def items():
    with open('items.json', 'r') as f:
        items = json.load(f)
        return render_template('items.html', items=items)

@app.get('/products')
def products():
    source = request.args.get('source')
    id = request.args.get('id')

    if source == 'json':
        data = []
        with open('products.json', 'r') as f:
            data = json.load(f)
        if id:
            data = [row for row in data if row['id'] == int(id)]

        return render_template('product_display.html', data='no product' if len(data) == 0 else data)

    if source == 'csv':
        data = []
        with open('products.csv', mode='r', newline='') as f:
            data = csv.DictReader(f)
            data = [row for row in data]
        if id:
            data = [row for row in data if row['id'] == id]

        return render_template('product_display.html', data='no product' if len(data) == 0 else data)
    
    if source == 'db':
        data = []
        try:
            with sqlite3.connect('products.db') as db:
                cursor = db.cursor()

                if id:
                    cursor.execute('SELECT * FROM Products WHERE id=?', (id,))
                else:
                    cursor.execute('SELECT * FROM Products')

                rows = cursor.fetchall()
                for row in rows:
                    data.append({
                        "id": row[0],
                        "name": row[1],
                        "category": row[2],
                        "price": row[3]
                    })

                return render_template('product_display.html', data='no product' if len(data) == 0 else data)
        except Exception as e:
            render_template('product_display.html', data='error')

    return render_template('product_display.html', data='error')

if __name__ == '__main__':
    app.run(debug=True, port=5000)
