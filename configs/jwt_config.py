from os import getenv as get

JWT_CONFIG = {
    'secret': get('URLINK_JWT_SECRET'),
    'algorithm': get('URLINK_JWT_ALGORITHM'),
}