from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from .resources import ns, Login,Signup  
from .extensions import  api,db  
app = Flask(__name__)
url = 'mysql://root:12345@127.0.0.1:3306/dbname'
app.config['SQLALCHEMY_DATABASE_URI'] = url

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 

db.init_app(app)
api.init_app(app)

api.add_resource(Signup, '/signup')
api.add_resource(Login, '/login')
api.add_namespace(ns)
if __name__ == '__main__':
    app.run(debug=True)




