from flask import Flask, render_template, request, redirect, url_for
import flask_login
import pymongo
import os
import flask_login
from dotenv import load_dotenv
load_dotenv()

# create the flask app and set the session
app = Flask(__name__)
app.secret_key = os.environ.get('SECRET_KEY')

client = pymongo.MongoClient(os.environ.get('MONGO_URI'))


# "magic code" -- boilerplate
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)