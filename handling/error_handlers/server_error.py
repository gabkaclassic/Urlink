from app.urlink import app
from werkzeug.exceptions import InternalServerError
from flask import Response
@app.errorhandler(InternalServerError)
def handle(error):


    return Response("Invalid token", status=InternalServerError.code)
