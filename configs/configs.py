from pathlib import Path

from dotenv import load_dotenv as load
from os import getenv as get

BASE_DIR = Path(__file__).resolve().parent.parent
load(BASE_DIR / 'dev.env')

DEBUG = get('DEBUG')

JWT_CONFIG = {
    'secret': get('URLINK_JWT_SECRET'),
    'algorithm': get('URLINK_JWT_ALGORITHM'),
}

DB_CONFIG = {
    'password': get('URLINK_DB_PASSWORD'),
    'user': get('URLINK_DB_USER'),
    'name': get('URLINK_DB_NAME'),
    'host': get('URLINK_DB_HOST'),
    'port': get('URLINK_DB_PORT'),
}
