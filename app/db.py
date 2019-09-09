from pymongo import MongoClient
from cfenv import AppEnv

try:
    env = AppEnv()
    mlab = env.get_service(label='mlab')
    conn_str = mlab.credentials['uri']
except:
    pass

def get_db():
    try:
        db = MongoClient(conn_str).get_database()
    except:
        client = MongoClient('localhost', 27017)
        db = client.location
        
    return db.locations
