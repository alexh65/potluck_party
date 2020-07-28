from flask import request, g, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from flask_httpauth import HTTPBasicAuth
auth = HTTPBasicAuth()

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

    if User_info.query.filter_by(email_address = content[email_address]).first is not None:
      abort(400)
    
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

    return "Received user info", 201

@app.route('/token')
@auth.login_required
def get_auth_token():
  token = g.user.generate_auth_token()
  return jsonify({'token': token.decode('ascii')})

@auth.verify_password
def verify_password(username_or_token, password):
  # first try to authenticate by token
    user = User_login.verify_auth_token(username_or_token)
    if not user:
        # try to authenticate with username/password
        user = User_login.query.filter_by(username = username_or_token).first()
        if not user or not check_password_hash(user.password, password):
            return False
    g.user = user
    return True

@app.route('/login', methods=['POST'])
def login():
  content = request.get_json()
  request_username = content['username']
  request_password = content['password']

  valid = verify_password(request_username, request_password)

  if valid:
    print('---------------Valid login info----------------')
    token = g.user.generate_auth_token()
    return jsonify({'token': token.decode('ascii')})
  
  print('---------------Invalid login info----------------')
  return 'The username or password is invalid', 400
