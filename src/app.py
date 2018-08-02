from flask import Flask
import time
import logging
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, Worlds!'

@app.route('/slow')
def hello_slow_world():
    logger = logging.getLogger('app')
    logger.warning("starting")
    time.sleep(6)
    logger.warning("done sleeping")
    return 'Hello, slow Worlds!'