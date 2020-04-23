from flask import Flask, render_template, request, redirect, url_for
import flask_login
import pymongo
import os
import flask_login
from passlib.hash import pbkdf2_sha256
from dotenv import load_dotenv
load_dotenv()

# create the flask app and set the session
app = Flask(__name__)
app.secret_key = os.environ.get('SECRET_KEY')

client = pymongo.MongoClient(os.environ.get('MONGO_URI'))
DB_NAME = 'my_app'

# create the login manager
login_manager = flask_login.LoginManager()
login_manager.init_app(app)


class User(flask_login.UserMixin):
    pass


def encrypt_password(plaintext):
    return pbkdf2_sha256.hash(plaintext)


def verify_password(plaintext, encrypted):
    return pbkdf2_sha256.verify(plaintext, encrypted)


@login_manager.user_loader
def user_loader(email):

    # attempt to get the user
    user_in_db = client[DB_NAME]['users'].find_one({
        "email": email
    })

    user = User()
    user.id = user_in_db['email']

    # if an user is found
    if user:
        return user
    else:
        return None


@app.route('/login')
def login():
    return render_template('login.template.html')


@app.route('/login', methods=["POST"])
def process_login():
    user_in_db = client[DB_NAME]['users'].find_one({
        "email": request.form.get('email')
    })

    user = User()
    user.id = user_in_db['email']
    if verify_password(request.form.get('password'), user_in_db['password']):
        flask_login.login_user(user)
        return "logged in successfully"

    return "logged in failure"


@app.route('/protected')
@flask_login.login_required
def protected():
    return 'Logged in as: ' + flask_login.current_user.id


# "magic code" -- boilerplate
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)