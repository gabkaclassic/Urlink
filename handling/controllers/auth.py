from app.urlink import app
from flask import redirect, request
from handling.data.models.accounts import Account

from handling.data.models import accounts


@app.route('/auth', methods=['GET'])
async def auth():
    id = request.environ['id']
    authorities = request.environ['role']

    if not Account.exists_by_id(id) and 'ADMIN' not in authorities:
        Account.create_user(id)

    return redirect('/statistics')
