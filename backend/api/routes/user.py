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
      password = generate_password_hash(content['password']),
      role = 'ROLE_USER'
    )

    db.session.add(user_login)
    db.session.flush()
    
    db.session.commit()
    print(user_info)

    return "Received user info"

@app.route('/login', methods=['POST'])
def checkUser():
  content = request.get_json()
  request_username = content['username']
  
  password = content['password']
  print('----Received password:', password)
  stored_pass = User_login.query.filter_by(username=request_username).first().password
  print('----Stored password:', stored_pass)

  if check_password_hash(stored_pass, password):
    return "The password is correct", 200
  
  return "The password is incorrect", 400
