from flask import (Blueprint, request)
from . import db

"""Add the API to the app blueprint"""
a = Blueprint('api', __name__)

@a.route('/api', methods=['POST'])
def api():
    """Create an API app route. Format the request as a JSON object and insert
    into the DB"""
    #TODO: Add request validation, error handling and better return status
    #descriptions

    """Insert the record that is passed from the API user into the DB and assign
    the inserted ID to an 'id' variable"""
    id = db.get_db().insert_one(request.get_json()).inserted_id
    
    """Return a success message to the API user"""
    return f"Success inserted {id}"
