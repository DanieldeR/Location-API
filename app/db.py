from pymongo import MongoClient
from cfenv import AppEnv

#TODO: Make this more robust and/or dynamic for other DB types
"""Try and pull the CF environment variables for mlab"""
try:
    env = AppEnv()
    mlab = env.get_service(label='mlab')
    conn_str = mlab.credentials['uri']
except:
    pass


def get_db():
    """Return DB connection information. When running on CF, return the CF
    details, otherwise return local DB connection for testing"""

    #TODO: Remove local testing for production environment
    try:
        db = MongoClient(conn_str + '?retryWrites=false').get_database()
    except:
        client = MongoClient('localhost', 27017)
        db = client.location
    
    #TODO: Refactor to accept dynamic DB locations. Maybe a class to abstract
    # getting DB tables, etc...
    return db.locations
