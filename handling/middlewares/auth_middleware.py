from handling.utils.jwt import validate, extract_user_info as extract_info
from flask import session
from flask import Response as response
from flask import redirect
from flask_api.status import (
    HTTP_401_UNAUTHORIZED as unauthorized,
    HTTP_200_OK as OK,
)
from werkzeug.wrappers import Request, Response


class AuthMiddleware:

    def __init__(self, app):
        self.app = app

    def __call__(self, environ, start_response):

        request = Request(environ)
        token = request.authorization.token
        if validate(token):
            environ['id'], environ['role'] = extract_info(token)
            return self.app(environ, start_response)

        return Response('Authentication failed', status=unauthorized, mimetype='json')
