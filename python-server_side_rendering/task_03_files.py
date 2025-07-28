from flask import Flask, render_template, request
import json
import csv

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
    type = request.args.get('source')

    if type == 'json':
        data = []
        with open('products.json', 'r') as f:
            data = json.load(f)
        if request.args.get('id'):
            data = [row for row in data if row['id'] == int(request.args.get('id'))]

        return render_template('product_display.html', data='no product' if len(data) == 0 else data)

    if request.args.get('source') == 'csv':
        data = []
        with open('products.csv', mode='r', newline='') as f:
            data = csv.DictReader(f)
            data = [row for row in data]
        if request.args.get('id'):
            data = [row for row in data if row['id'] == request.args.get('id')]

        return render_template('product_display.html', data='no product' if len(data) == 0 else data)

    return render_template('product_display.html', data='error')

if __name__ == '__main__':
    app.run(debug=True, port=5000)
