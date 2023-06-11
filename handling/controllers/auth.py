from app.urlink import app
from flask import session, redirect, Response as response, request
from handling.utils.jwt import extract_user_id as extract_id
from flask_api.status import (
    HTTP_200_OK as OK,
)
@app.route('/auth', methods=['GET'])
async def auth():


    id = request.environ['id']
    print(id)

    return response(status=OK)

    # if id is not None:
    #     return redirect('/statistics')
    # else:
    #     response(status=401)
