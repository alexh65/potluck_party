from datetime import date
# from sqlalchemy import Relationship

from app import db


class Recipe(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  user_id = db.Column(db.Integer, db.ForeignKey('user_info.id', onupdate='CASCADE', ondelete='CASCADE'), nullable=False)
  date_created = db.Column(db.Date, nullable=False, default=date.today())
  recipe_desc = db.Column(db.String(225))
  recipe_result_pic = db.Column(db.String(200))
  prep_time = db.Column(db.Integer)
  cook_time = db.Column(db.Integer)
  ingredients = db.relationship('Recipe_ingredient', backref='recipe', lazy='select')
  steps = db.relationship('Recipe_step', backref='recipe', lazy='select')

  def __repr__(self):
    return 'Recipe - ' + str(id) + ' by User ' + str(user_id)

class Ingredient(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  ingredient_name = db.Column(db.String(50), nullable=False)
  calories_per_serving = db.Column(db.Integer)
  serving_amount = db.Column(db.String(10))
  recipes = db.relationship('Recipe_ingredient', backref='recipe', lazy='select')

  def __repr__(self):
    return 'Ingredient - ' + self.ingredient_name

class Recipe_ingredient(db.Model):
  recipe_id = db.Column(db.Integer, db.ForeignKey('recipe.id', onupdate='CASCADE', ondelete='CASCADE'), primary_key = True,)
  ingredient_id = db.Column(db.Integer, db.ForeignKey('ingredient.id', onupdate='CASCADE', ondelete='CASCADE'), primary_key = True)
  amount = db.Column(db.Integer, nullable=False)
  amount_unit = db.Column(db.String(20), nullable=False)
  
  def __repr__(self):
    return 'Ingredient - ' + str(self.ingredient_id)+' for recipe ' + str(self.recipe_id)

class Recipe_step(db.Model):
  recipe_id = db.Column(db.Integer,  db.ForeignKey('recipe.id', onupdate='CASCADE', ondelete='CASCADE'), primary_key = True,)
  step_no = db.Column(db.Integer, primary_key=True)
  step_desc = db.Column(db.String(200), nullable=False)

  def __repr__(self):
    return 'Step - no.' + str(step.no) + ' for Recipe ' + str(recipe_id)