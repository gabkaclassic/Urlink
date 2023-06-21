from os import getenv as get

DB_CONFIG = {
    'password': get('URLINK_DB_PASSWORD'),
    'user': get('URLINK_DB_USER'),
    'name': get('URLINK_DB_NAME'),
    'host': get('URLINK_DB_HOST'),
    'port': get('URLINK_DB_PORT'),
}

DB_URI = 'postgresql://%(user)s:%(password)s@%(host)s:%(port)s/%(name)s' % DB_CONFIG
