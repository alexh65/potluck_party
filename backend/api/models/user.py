from sqlalchemy import CheckConstraint

from api import db


class User_info(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  first_name = db.Column(db.String(20), nullable=False)
  last_name = db.Column(db.String(30))
  email_address = db.Column(db.String(50), unique=True)
  user_bio = db.Column(db.String(225))
  profile_pic = db.Column(db.String(225))

  def __repr__(self):
    return 'User ' + str(self.id) + ' - ' + self.email_address


class User_login(db.Model):
  user_id = db.Column(db.Integer, db.ForeignKey('user_info.id', onupdate='CASCADE', ondelete='CASCADE'),  primary_key=True,)
  username = db.Column(db.String(20), unique=True, nullable=False)
  password = db.Column(db.String(128), nullable=False)
  role = db.Column(db.String(50), nullable=False)

  def __repr__(self):
    return 'Login for User ' + str(self.user_id) + ' - ' + self.username


class Friends(db.Model):
  friend1_id = db.Column(db.Integer, db.ForeignKey('user_info.id', onupdate='CASCADE', ondelete='CASCADE'), primary_key=True,)
  friend2_id = db.Column(db.Integer, db.ForeignKey('user_info.id', onupdate='CASCADE', ondelete='CASCADE'), primary_key=True,)

  __table_args__ = (
    CheckConstraint(friend1_id < friend2_id, name='firstIdIsLessThanSecond'),
  )

  def __repr__(self):
    return 'Friends - ' + str(friend1_id) + ' + ' + str(friend2_id)