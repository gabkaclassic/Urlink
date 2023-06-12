from app.urlink import app
from flask import request, Response
from handling.data.models.links import Link
from flask_api.status import HTTP_200_OK as OK


@app.route("/reduce", methods=['POST'])
def reduce():
    id = request.environ['id']
    original = request.json['url']
    title = request.json['title']
    formatted = Link.create(id, original, title,  request.root_url)

    return Response(formatted, status=OK)
