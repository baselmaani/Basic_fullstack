from flask_restful import reqparse


signup_parser = reqparse.RequestParser()
signup_parser.add_argument('username', type=str, required=True, help='Username is required')
signup_parser.add_argument('password', type=str, required=True, help='Password is required')



login_parser = reqparse.RequestParser()
login_parser.add_argument('username', type=str, required=True, help='Username is required')
login_parser.add_argument('password', type=str, required=True, help='Password is required')
