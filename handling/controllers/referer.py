from app.urlink import app
from flask import request, redirect
from handling.utils.statistics import registration_visit


@app.route('/ref/<formatted>')
async def referer():
    formatted = request.view_args['formatted']
    ip = request.remote_addr
    original = await registration_visit(ip, formatted)

    return redirect(original)
