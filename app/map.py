from flask import (Blueprint, request, jsonify)
from . import db

bp = Blueprint('map', __name__)

@bp.route('/')#, requests=['POST'])
def index():
    #some_string = request.args.get('test')

    some_data = db.get_db().find_one()

    print(some_data['_id'])
    return str(some_data['_id'])
