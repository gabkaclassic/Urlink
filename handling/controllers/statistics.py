import asyncio

from app.urlink import app
from flask import request
from flask import jsonify as json
from handling.utils.statistics import get_statistics


@app.route('/statistics', methods=['GET'])
def statistics():
    id = request.environ['id']
    return json(asyncio.run(get_statistics(id)))
