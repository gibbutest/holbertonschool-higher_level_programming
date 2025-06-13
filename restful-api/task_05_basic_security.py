from flask import Flask, jsonify, request
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import (JWTManager, create_access_token, jwt_required, get_jwt_identity)

app = Flask(__name__)
auth = HTTPBasicAuth()
app.config['JWT_SECRET_KEY'] = 'hamburgercheeseburgerbigmacwhopper'
jwt = JWTManager(app)

users = {
    'user1': {
        'username': 'user1',
        'password': generate_password_hash('password'),
        'role': 'user'
    },
    'admin1': {
        'username': 'admin1',
        'password': generate_password_hash('password'),
        'role': 'admin'
    }
}

@auth.verify_password
def verify_password(username, password):
    user = users.get(username)
    return user if user and check_password_hash(user['password'], password) else None

@app.get('/basic-protected')
@auth.login_required
def basic_protected():
    return 'Basic Auth: Access Granted'

@app.post('/login')
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    user = users.get(username)
    if user and check_password_hash(user['password'], password):
        identity = {
            'username': username,
            'role': user['role']
        }
        access_token = create_access_token(identity=identity)
        return jsonify(access_token=access_token)
    return jsonify({'error': 'Invalid credentials'}), 401

@app.get('/jwt-protected')
@jwt_required()
def jwt_protected():
    return 'JWT Auth: Access Granted'

@app.get('/admin-only')
@jwt_required()
def admin_only():
    current_user = get_jwt_identity()
    if current_user['role'] == 'admin':
        return 'Admin Access: Granted'
    else:
        return jsonify({'error': 'Admin access required'}), 403

@jwt.unauthorized_loader
def handle_unauthorized_error():
    return jsonify({'error': 'Missing or invalid token'}), 401

@jwt.invalid_token_loader
def handle_invalid_token_error():
    return jsonify({'error': 'Invalid token'}), 401

@jwt.expired_token_loader
def handle_expired_token_error():
    return jsonify({'error': 'Token has expired'}), 401

@jwt.revoked_token_loader
def handle_revoked_token_error():
    return jsonify({'error': 'Token has been revoked'}), 401

@jwt.needs_fresh_token_loader
def handle_needs_fresh_token_error():
    return jsonify({'error': 'Fresh token required'}), 401

if __name__ == '__main__':
    app.run()