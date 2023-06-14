from app.urlink import app
from configs.configs import DEBUG, PORT, HOST

if __name__ == '__main__':
    app.run(debug=DEBUG, port=PORT, host=HOST)


