from flask_restx import fields
from .extensions import  api

user_signup_model=api.model('UserSignup',{
    'id':fields.Integer(readonly=True),
    'username':fields.String(required=True),
    'email':fields.String(required=True),
    'password':fields.String(required=True),
    'role':fields.String(required=True)
    })

user_login_model=api.model('UserLogin',{
    
    'username':fields.String(required=True),
    'password':fields.String(required=True)
    })
