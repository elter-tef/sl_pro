from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()
class User(db.Model):
	__tablename__ = 'user'
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	login =  db.Column(db.Text, nullable=False)
	addresses = db.relationship('Address', backref='user',
								lazy='dynamic')


class Address(db.Model):
	__tablename__ = 'address'
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	email = db.Column(db.String(50))
	user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
