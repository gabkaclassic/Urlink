from app.urlink import app
from configs.app_config import DEBUG, PORT, HOST, KEY, CERT

if __name__ == '__main__':
    app.run(debug=DEBUG, port=PORT, host=HOST, ssl_context=(CERT, KEY))


