from flask import (Blueprint, request)
from . import db

a = Blueprint('api', __name__)
  
@a.route('/api', methods=['POST'])
def api():
    #some_string = request.args.get('test')
    id = db.get_db().insert_one(request.get_json()).inserted_id
    
    return f"Success inserted {id}"
