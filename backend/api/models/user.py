from sqlalchemy import CheckConstraint
from itsdangerous import (TimedJSONWebSignatureSerializer as Serializer, BadSignature, SignatureExpired)
from api import app, db


class User_info(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  first_name = db.Column(db.String(20), nullable=False)
  last_name = db.Column(db.String(30))
  email_address = db.Column(db.String(50), unique=True)
  user_bio = db.Column(db.String(225))
  profile_pic = db.Column(db.String(225))

  def __repr__(self):
    return 'User info: ' + str(self.id) + ' - ' + self.email_address


class User_login(db.Model):
  user_id = db.Column(db.Integer, db.ForeignKey('user_info.id', onupdate='CASCADE', ondelete='CASCADE'),  primary_key=True,)
  username = db.Column(db.String(20), unique=True, nullable=False)
  password = db.Column(db.String(128), nullable=False)
  role = db.Column(db.String(50), nullable=False)

  # The token is an encrypted version of a dictionary that has the id of the user
  def generate_auth_token(self, expiration = 10800):
    s = Serializer(app.config['SECRET_KEY'], expires_in = expiration)
    return s.dumps({'id': self.user_id})
  
  @staticmethod
  def verify_auth_token(token):
    print('------In verify_auth_token-------')
    s = Serializer(app.config['SECRET_KEY'])
    print(token)
    try:
      data = s.loads(token)
    except SignatureExpired:
      print('Signature Expired')
      return None # valid token, but expired
    except BadSignature:
      print('Bad Signature')
      return False # invalid token
    print('Everything ok')
    return User_login.query.get(data['id'])

  def __repr__(self):
    return 'User login: ' + str(self.user_id) + ' - ' + self.username


class Friends(db.Model):
  friend1_id = db.Column(db.Integer, db.ForeignKey('user_info.id', onupdate='CASCADE', ondelete='CASCADE'), primary_key=True,)
  friend2_id = db.Column(db.Integer, db.ForeignKey('user_info.id', onupdate='CASCADE', ondelete='CASCADE'), primary_key=True,)

  __table_args__ = (
    CheckConstraint(friend1_id < friend2_id, name='firstIdIsLessThanSecond'),
  )

  def __repr__(self):
    return 'Friends - ' + str(friend1_id) + ' + ' + str(friend2_id)