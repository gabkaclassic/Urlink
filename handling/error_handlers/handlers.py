from app.urlink import app
from werkzeug.exceptions import HTTPException


# @app.errorhandler(HTTPException)
# def unauthorized_handler(error):
#     response = error.get_response()
#     response.data = {
#         "code": error.code,
#         "name": error.name,
#         "description": error.description,
#     }
#     response.content_type = 'application/json'
#
#     return response
