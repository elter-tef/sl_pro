from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()
class User(db.Model):
	__tablename__ = 'user'
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	login =  db.Column(db.Text, nullable=False)
	#User_Character = db.relationship('UserCharacter', back_populates='user', lazy='dynamic')


