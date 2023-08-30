import jwt
from datetime import datetime, timedelta
from werkzeug.security import generate_password_hash, check_password_hash
import app

def generate_token(user_id):
    payload = {
        'exp': datetime.utcnow() + timedelta(days=1),
        'iat': datetime.utcnow(),
        'sub': user_id,
    }
    return jwt.encode(payload, app.config['SECRET_KEY'], algorithm='HS256')


def decode_token(token):
    payload = jwt.decode(token, app.config['SECRET_KEY'], algorithms=['HS256'])
    return payload['sub']

def hash_password(password):
    return generate_password_hash(password, method='sha256')

def check_password(password, hashed_password):
    return check_password_hash(hashed_password, password)

