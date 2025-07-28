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

@app.get('/products')
def data():
    source = request.args.get('source')
    id = request.args.get('id')
    data = []

    if source == 'json':
        try:
            with open('products.json') as f:
                data = json.load(f)
        except Exception as e:
            return f"Error loading JSON: {e}", 500

    elif source == 'csv':
        try:
            with open('products.csv') as f:
                reader = csv.DictReader(f)
                data = list(reader)
        except Exception as e:
            return f"Error loading CSV: {e}", 500

    elif source == 'sql':
        try:
            conn = sqlite3.connect("products.db")
            conn.row_factory = sqlite3.Row
            cursor = conn.cursor()
            if id:
                cursor.execute("SELECT * FROM Products WHERE id = ?", (id,))
            else:
                cursor.execute("SELECT * FROM Products")
            data = cursor.fetchall()
        except Exception as e:
            return f"Error loading SQL: {e}", 500
    else:
        return "Wrong source"

    if id and not data:
        return "Product not found"

    return render_template("product_display.html", products=data)


if __name__ == '__main__':
    app.run(debug=True, port=5000)