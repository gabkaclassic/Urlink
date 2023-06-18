from app.urlink import app
from werkzeug.exceptions import NotFound
from flask import Response


@app.errorhandler(NotFound)
def handle(error):
    return Response("Unknown page", status=NotFound.code)
