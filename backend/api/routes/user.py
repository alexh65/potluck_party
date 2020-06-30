from flask import request
from werkzeug.security import generate_password_hash, check_password_hash

from api import app, db
from api.models.user import User_info, User_login

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
    db.session.add(user_info)
    db.session.flush()

    user_login = User_login(
      user_id = user_info.id,
      username = content['username'],
      password = content['password'],
      role = 'ROLE_USER'
    )

    db.session.add(user_login)
    db.session.commit()
    print(user_info)

    return "Received user info"

