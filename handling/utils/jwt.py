from jwt import decode, ExpiredSignatureError, InvalidTokenError
from configs.configs import JWT_CONFIG
from datetime import datetime as date


def decode_token(token: str):
    try:
        return decode(token, SECRET, algorithms=[ALGORITHM])
    except InvalidTokenError:
        raise InvalidTokenError


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

    try:
        decoded = decode_token(token)
    except InvalidTokenError:
        return False

    return not (locked(decoded) or expired(decoded))


SECRET = JWT_CONFIG['secret']
ALGORITHM = JWT_CONFIG['algorithm']
