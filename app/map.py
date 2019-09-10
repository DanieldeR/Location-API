from flask import (Blueprint, request, jsonify, render_template)
from . import db
from pymongo import DESCENDING

bp = Blueprint('map', __name__)

@bp.route('/')#, requests=['POST'])
def index():
    resolution = 2

    latest_location = db.get_db().find_one({}, sort=[('_id', DESCENDING)])

    location = {}

    clean_location = latest_location['location'].split(',')

    location['lat'] = round(float(clean_location[0]), resolution)
    location['lon'] = round(float(clean_location[1]), resolution)

    return render_template("map.html", location=location)
