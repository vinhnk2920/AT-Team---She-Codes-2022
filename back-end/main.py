import datetime
import os
import random
from functools import wraps

import jwt
from flask import Flask, request, jsonify, make_response, json
from werkzeug.security import check_password_hash, generate_password_hash

from Model.model import LoginInformation, MemberOfProject, Project, Quote

app = Flask(__name__)

# Routes

app.config['SECRET_KEY'] = 'NoBaABRXyMcHvWnCTLtkpL0BX7iOONf9'


# decorator for verifying the JWT
def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None
        if 'Authorization' in request.headers:
            token = request.headers['Authorization']
        if not token:
            return json.jsonify({
                'success': False,
                'message': 'Token is missing!!',
                'data': []
            })

        try:
            data = jwt.decode(token, app.config['SECRET_KEY'], algorithms=['HS256'])
            current_user = LoginInformation.select().where(LoginInformation.password == data['password']).first()
        except Exception as e:
            print(e)
            return json.jsonify({
                'success': False,
                'message': 'Token is invalid!!',
                'data': []
            })
        return f(current_user, *args, **kwargs)
        # return current_user

    return decorated


# route for logging user in
@app.route('/login', methods=['POST'])
def login():
    auth = request.json

    if not auth or not auth.get('username') or not auth.get('password'):
        return json.jsonify({
            'success': False,
            'message': 'Missing some params!!',
            'data': []
        })
    user = LoginInformation.select().where(LoginInformation.username == auth.get('username')).first()

    if not user:
        return json.jsonify({
            'success': False,
            'message': 'User does not exist !!',
            'data': []
        })

    if check_password_hash(user.password, auth.get('password')):
        token = jwt.encode({
            'password': user.password
        }, app.config['SECRET_KEY'])
        return json.jsonify({
            'success': True,
            'message': 'Login successful!!',
            'token': token
        })

    return json.jsonify({
        'success': False,
        'message': 'Wrong password!!',
        'data': []
    })


# signup route
@app.route('/signup', methods=['POST'])
def signup():
    data = request.json

    username = data.get('username')
    password = data.get('password')

    # checking for existing user
    user = LoginInformation.select().where(LoginInformation.username == username).first()

    if user:
        return json.jsonify({
            'success': False,
            'message': 'User already exists. Please Log in.',
            'data': []
        })
    try:
        # insert user
        data_save = {
            'username': username,
            'password': generate_password_hash(password)
        }
        LoginInformation.create(**data_save)

        return json.jsonify({
            'success': True,
            'message': 'Successfully registered!',
            'data': []
        })
    except Exception as e:
        return json.jsonify({
            'success': True,
            'message': 'Fail registered!',
            'data': []
        })


@app.route('/quotes/get', methods=['GET'])
def get_quote():
    try:
        count_quote = Quote.select().count()
        random_num = random.randrange(1, count_quote)
        quote = Quote.select(Quote.id, Quote.content, Quote.author).where(Quote.id == random_num).first()
        return json.jsonify({
            'success': True,
            'message': 'Success for get quote!',
            'data': {
                "id": quote.id,
                "content": quote.content,
                "author": quote.author
            }
        })
    except Exception as e:
        print(e)
        return json.jsonify({
            'success': True,
            'message': 'Fail to get quote!',
            'data': []
        })


# users
@app.route('/users/projects', methods=['GET'])
@token_required
def get_user_project(user_id):
    try:
        projects = MemberOfProject.select(MemberOfProject.shop_code) \
            .join(Project, on=(Project.id == MemberOfProject.project_id)) \
            .where(MemberOfProject.id == user_id).dicts()
        return json.jsonify({
            'success': True,
            'message': 'Fail when get projects of user!',
            'data': projects
        })
    except Exception as e:
        print(e)
        return json.jsonify({
            'success': True,
            'message': 'Fail when get projects of user!',
            'data': []
        })


API_HANDLE_HOST = os.getenv('NGINX_VHOST', '127.0.0.1')
API_HANDLE_PORT = os.getenv('NGINX_PORT', 5000)

if __name__ == '__main__':
    app.run(host=API_HANDLE_HOST, port=API_HANDLE_PORT)
