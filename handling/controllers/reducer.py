from app.urlink import app
from flask import request, Response
from handling.data.models.links import Link
from flask_api.status import HTTP_200_OK as OK, HTTP_400_BAD_REQUEST as BAD
from handling.utils.pinger import ping

@app.route("/reduce", methods=['POST'])
def reduce():

    original = request.json['url']

    if not ping(original):
        return Response('Url is invalid', status=BAD)

    id = request.environ['id']
    title = request.json['title']
    formatted = Link.create(id, original, title,  request.root_url)

    return Response(formatted, status=OK)
