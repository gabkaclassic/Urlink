from app.urlink import app
from werkzeug.exceptions import Unauthorized
from flask import Response
@app.errorhandler(Unauthorized)
def handle(error):
    return Response("Invalid token", status=Unauthorized.code)
