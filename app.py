from flask import Flask
import os
from cfenv import AppEnv

app = Flask(__name__)

cf_port = os.getenv("PORT")

env = AppEnv()
mlab = env.get_service(label='mlab')


@app.route('/')
def hello_world():
    return f"I'm running! On port {cf_port}, {mlab.credentials['uri']}"

if __name__ == '__main__':
    if cf_port is None:
        app.run(host = '0.0.0.0', port=5000, debug = True)
    else:
        app.run(host = '0.0.0.0', port=int(cf_port), debug=True)
