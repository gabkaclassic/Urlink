from alembic.util import status
from flask_api.status import (
    HTTP_401_UNAUTHORIZED as unauthorized,
)
from werkzeug.wrappers import Request, Response

from handling.utils.jwt import validate, extract_user_info as extract_info


class AuthMiddleware:

    def __init__(self, app):
        self.app = app

    def __call__(self, environ, start_response):

        request = Request(environ)


        if request.path.startswith('/ref/'):
            return self.app(environ, start_response)

        if request.authorization is None:
            return start_response(request, status=401)

        token = request.authorization.token

        if validate(token):
            environ['id'], environ['role'] = extract_info(token)
            return self.app(environ, start_response)

        return start_response(request)
