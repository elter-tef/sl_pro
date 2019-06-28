from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()
class User(db.Model):
	__tablename__ = 'user'
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	login =  db.Column(db.Text, nullable=False)
	items_user = db.relationship('ItemUser', backref='user',
								lazy='dynamic')


class Item(db.Model):
	__tablename__ = 'item'
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	name = db.Column(db.String(50))
	user_item = db.relationship('ItemUser', backref='item',
								lazy='dynamic')

class ItemUser(db.Model):
	__tablename__ = 'item_user'
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
	item_id = db.Column(db.Integer, db.ForeignKey('item.id'))

