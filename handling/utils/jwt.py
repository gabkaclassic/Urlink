from jwt import decode
from configs.configs import JWT_CONFIG
from datetime import datetime as date


def decode_token(token: str):
    return decode(token, SECRET, algorithms=[ALGORITHM])


def expired(token):
    return date.fromtimestamp(token['exp']) < date.now()


def locked(token):
    return 'LOCKED' in token['role']


def extract_user_info(token):
    decoded = decode_token(token)
    return decoded['id'], decoded['role']


def validate(token: str):
    if token is None:
        return False

    decoded = decode_token(token)

    return not (locked(decoded) or expired(decoded))


SECRET = JWT_CONFIG['secret']
ALGORITHM = JWT_CONFIG['algorithm']
