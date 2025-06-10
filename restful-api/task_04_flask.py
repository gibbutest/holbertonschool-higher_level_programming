from flask import Flask, jsonify, request

db = {}

app = Flask(__name__)

@app.get('/')
def home():
    return "Welcome to the Flask API!"

@app.get('/data')
def data():
    return jsonify(list(db.keys()))

@app.get('/status')
def status():
    return 'OK'

@app.get('/users/<username>')
def getUser(username):
    user = db.get(username)

    if not user:
        return jsonify({'error': 'User not found'}), 404

    return jsonify(user)

@app.post('/add_user')
def addUser():
    body = request.get_json()

    if not body or "username" not in body:
        return jsonify({"error": "Username is required"}), 400

    # This whole key = username but still keep the username is so stupid.
    username = body["username"]
    db[username] = body

    return jsonify({"message": "User added", "user": body}), 201

if __name__ == '__main__':
    app.run()