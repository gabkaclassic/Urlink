from app.urlink import app
from flask import request, redirect
from handling.utils.statistics import registration_visit


@app.route('/ref/<key>')
async def referer(key):

    ip = request.remote_addr
    original = await registration_visit(ip, key)

    return redirect(original)
