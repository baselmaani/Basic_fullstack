from flask_restx import Resource, Namespace
from werkzeug.security import generate_password_hash, check_password_hash
from flask_restful import Api, Resource, reqparse
from .services import generate_token, hash_password, check_password
from .models import User
from .extensions import db, api
from .requestParsing import signup_parser, login_parser
from .api_models import user_signup_model, user_login_model

ns=Namespace('auth',description='Authentication related operations')

@ns.route('/signup')
class Signup(Resource):
    @ns.expect(user_signup_model)
    def post(self):
        data = signup_parser.parse_args()
        username = data['username']
        password = data['password']

        existing_user = User.query.filter_by(username=username).first()
        if existing_user:
            return {'message': 'Username already exists'}, 400

     
        hashed_password = hash_password(password)

     
        new_user = User(username=username, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()

        return {'message': 'User created successfully'}, 201


@ns.route('/login')
class Login(Resource):
    @ns.expect(user_login_model)
    def post(self):
        data = login_parser.parse_args()
        username = data['username']
        password = data['password']

    
        user = User.query.filter_by(username=username).first()

        if not user or not check_password(password, user.password):
            return {'message': 'Invalid username or password'}, 401

    
        token = generate_token(user.id)

        return {'message': 'Login successful', 'token': token}, 200

        