from flask_restx import Resource, Namespace
from werkzeug.security import generate_password_hash, check_password_hash
from .services import generate_token, hash_password, check_password
from .models import User
from .extensions import db, api
from .requestParsing import signup_parser, login_parser
from .api_models import user_signup_model, user_login_model

ns = Namespace('auth', description='Authentication related operations')

@ns.route('/signup')
class Signup(Resource):
    @ns.expect(user_signup_model)
    @ns.marshal_with(user_signup_model)
    def post(self):
        data = signup_parser.parse_args()
        username = data['username']
        password = data['password']
        email = data['email']
        role = data['role']
        hashed_password = hash_password(password)
        user = User.query.filter_by(username=username).first()
        if user:
            return {'message': 'User already exists'}, 400
        new_user = User(username=username, email=email, password=hashed_password, role=role)
        db.session.add(new_user)
        db.session.commit()
        print(new_user)
        return new_user, 201

@ns.route('/login')
class Login(Resource):
    @ns.expect(user_login_model)
    def post(self):
        data = login_parser.parse_args()
        email = data['email']
        password = data['password']
        user = User.query.filter_by(email=email).first()
        if not user:
            return {'message': 'User does not exist'}, 400
        if not check_password(password, user.password):
            return {'message': 'Incorrect password'}, 400
        token = generate_token(user.id)
        return {'token': token}, 200