from flask_restful import reqparse


signup_parser = reqparse.RequestParser()
signup_parser.add_argument('username', type=str, required=True, help='Username is required')
signup_parser.add_argument('password', type=str, required=True, help='Password is required')
signup_parser.add_argument('email', type=str, required=True, help='Email is required')
signup_parser.add_argument('role', type=str, required=True, help='Role is required')



login_parser = reqparse.RequestParser()
login_parser.add_argument('email', type=str, required=True, help='email is required')
login_parser.add_argument('password', type=str, required=True, help='Password is required')
