from app.urlink import app
from flask import redirect, request
from handling.data.services.accounts_service import *


@app.route('/auth', methods=['GET'])
async def auth():
    id = request.environ.get('id')
    authorities = request.environ.get('role')

    if (not exists_by_id(id)
        and authorities is not None
        and'ADMIN' not in authorities):
        Account.create_user(id)
    return redirect('/statistics')
