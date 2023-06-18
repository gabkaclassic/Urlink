from flask_api.status import (
    HTTP_401_UNAUTHORIZED as unauthorized,
)
from flask import abort, request, Response
from jwt import ExpiredSignatureError

from app.urlink import app
from handling.utils.jwt import validate, extract_user_info as extract_info


@app.before_request
def auth_middleware():

    abort(401)
    if request.path.startswith('/ref/'):
        return


    if request.authorization is None:
        abort(unauthorized)

    token = request.authorization.token

    if validate(token):
        try:
            request.environ['id'], request.environ['role'] = extract_info(token)
            return
        except ExpiredSignatureError:
            abort(401)
    abort(unauthorized)
