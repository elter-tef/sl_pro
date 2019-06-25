from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()
class User(db.Model):
	__tablename__ = 'user'
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	User_Character = db.relationship('UserCharacter', back_populates='user', lazy='dynamic')

class Character(db.Model):
	__tablename__ = 'character'
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	Character_User = db.relationship('UserCharacter', back_populates='character', lazy='dynamic')
class UserCharacter(db.Model):
	User_id = db.Column(db.Integer, db.ForeignKey(User.id), nullable=False)
	Character_id = db.Column(db.Integer, db.ForeignKey(Character.id), nullable=False)
	table_user = db.relationship('User', lazy='joined')
	table_character = db.relationship('Department', lazy='joined')
