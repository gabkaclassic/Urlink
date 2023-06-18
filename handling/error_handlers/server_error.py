from app.urlink import app
from werkzeug.exceptions import HTTPException
from flask import Response
import logging
@app.errorhandler(HTTPException)
def handle(error):

    logging.error(error.description)

    return Response("Server error", status=error.code)
