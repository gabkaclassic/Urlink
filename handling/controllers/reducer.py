from app.urlink import app
from flask import request, Response
from handling.data.models import Link
from flask_api.status import HTTP_200_OK as OK


@app.route("/reduce", methods=['POST'])
def reduce():
    id = request.environ['id']
    original = request.json['url']
    Link.create(original, id)

    return Response(status=OK)
