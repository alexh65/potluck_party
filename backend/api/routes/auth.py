from flask import request
from werkzeug.security import generate_password_hash, check_password_hash

from api import app
from api.models.user import User_info


@app.route('/')
def hello():
    return 'Hello World'


@app.route('/signup/info', methods=['POST'])
def make_new_user():
    content = request.get_json()
    user_info = User_info(
        first_name=content['first_name'],
        last_name=content['last_name'],
        email_address=content['email_address'],
        user_bio=content['user_bio'],
        profile_pic=content['profile_pic'],
    )
    # db.session.add(user_info)
    # db.session.commit()
    print(user_info)
    return "Received user info"


@app.route('/signup/login/', methods=['POST'])
def user_login():
    print('whatever')
