from pathlib import Path

from dotenv import load_dotenv as load
from os import getenv as get

BASE_DIR = Path(__file__).resolve().parent.parent
load(BASE_DIR / 'urlink.env')


DEBUG = get('URLINK_DEBUG')
PORT = get('URLINK_PORT')
HOST = get('URLINK_HOST')
KEY = get('URLINK_SSL_KEY')
CERT = get('URLINK_SSL_CERT')

