from werkzeug.exceptions import HTTPException


class UnauthorizedException(HTTPException):
    pass
