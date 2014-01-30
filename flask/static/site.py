import pymongo
from flask import Flask, request

DATABASE = "/tmp/personal_site.db"
DEBUG = True
SECRET_KEY = 'dev key'
USERNAME = 'admin'
PASSWORD = 'admin'

app = Flask(__name__)
app.config.from_object(__name__)

def connect_db():
    pass

if __name__ == '__main__':
    app.run()
