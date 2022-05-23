from flask import Flask
from flask_restful import Api
import random

app = Flask(__name__)
api = Api(app)

if __name__ == '__main__':
    app.run(host='localhost', port=5000)
