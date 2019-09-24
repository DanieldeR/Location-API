from flask import (Blueprint, request, jsonify, render_template)
from . import db
from pymongo import DESCENDING

"""Add 'map' to the app blueprint"""
bp = Blueprint('map', __name__)

@bp.route('/')
def index():
    """Read the latest location from the API and render the map template"""

    """Determine the amount of rounding to add - so as not to reveal my exact
    location"""
    resolution = 2

    """Pull the latest location from the DB, sort the ID descending to get
    latest"""
    latest_location = db.get_db().find_one({}, sort=[('_id', DESCENDING)])
    
    """Clean up the location that was returned by the DB"""
    #TODO: Add additional cleaning on DB insert, so we don't have to do it here
    location = {}
    clean_location = latest_location['location'].split(',')

    location['lat'] = round(float(clean_location[0]), resolution)
    location['lon'] = round(float(clean_location[1]), resolution)
    
    """Load the location data into the template and render it to the browser """
    return render_template("map.html", location=location)
