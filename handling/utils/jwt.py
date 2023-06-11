from jwt import decode
from configs.configs import JWT_CONFIG
from datetime import datetime as date


def decode_token(token: str):
    return decode(token, SECRET, algorithms=[ALGORITHM])


def extract_user_id(token: str):
    decoded = decode_token(token)
    return decoded['id']


def extract_user_autorities(token: str):
    decoded = decode_token(token)
    return decoded['role']


def expired(token):
    return date.fromtimestamp(token['exp']) < date.now()


def locked(token):
    return 'LOCKED' in token['role']


def validate(token: str):
    if token is None:
        return False

    decoded = decode_token(token)

    return not (locked(decoded) or expired(decoded))

def setup_session(session, token):
    session['id'] = extract_user_id(token)
    session['role'] = extract_user_autorities(token)

SECRET = JWT_CONFIG['secret']
ALGORITHM = JWT_CONFIG['algorithm']
