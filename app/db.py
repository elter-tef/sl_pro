from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()
from datetime import datetime
class User(db.Model):
	__tablename__ = 'user'
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	login =  db.Column(db.Text, nullable=False)
	character = db.relationship('Character', backref='user',
								lazy='dynamic')



class Character(db.Model):
	__tablename__ = 'character'
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	name = db.Column(db.Text, nullable=False)
	user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
	items_tb = db.relationship('ItemCharacter', backref='character', lazy='dynamic')
	informations_tb = db.relationship('InformationCharacter', backref='character', lazy='dynamic')
	room_tb = db.relationship('RoomCharacter', backref='character', lazy='dynamic')
	messages_tb = db.relationship('Messages', backref='character', lazy='dynamic')


class Item(db.Model):
	__tablename__ = 'item'
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	db.Column(db.Text, nullable=False)
	name = db.Column(db.Text, nullable=False)
	characters_tb = db.relationship('ItemCharacter', backref='item', lazy='dynamic')
	informations_tb = db.relationship('InformationItem', backref='item', lazy='dynamic')


class Information(db.Model):
	__tablename__ = 'information'
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	concept = db.Column(db.Text, nullable=False)
	text = db.Column(db.Text, nullable=False)
	characters_tb = db.relationship('InformationCharacter', backref='informations', lazy='dynamic')
	items_tb = db.relationship('InformationItem', backref='informations', lazy='dynamic')
	tags_master_tb = db.relationship('InformationTags_master', backref='information', lazy='dynamic')
	tags_semantic_tb = db.relationship('InformationTags_semantic', backref='information', lazy='dynamic')

class InformationItem(db.Model):
	__tablename__ = 'information_character'
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	character_id = db.Column(db.Integer, db.ForeignKey('information.id'))
	item_id = db.Column(db.Integer, db.ForeignKey('item.id'))


class InformationCharacter(db.Model):
	__tablename__ = 'information_character'
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	character_id = db.Column(db.Integer, db.ForeignKey('character.id'))
	information_id = db.Column(db.Integer, db.ForeignKey('information.id'))


class ItemCharacter(db.Model):
	__tablename__ = 'item_character'
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	number = db.Column(db.Integer,  default=1)
	character_id = db.Column(db.Integer, db.ForeignKey('character.id'))
	item_id = db.Column(db.Integer, db.ForeignKey('item.id'))


class Tags_master(db.Model):
	__tablename__ = 'tags_master'
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	tag = db.Column(db.Text, nullable=False)
	informations_tb = db.relationship('InformationTags_master', backref='tags_master', lazy='dynamic')


class OrderTags_master(db.Model):
	__tablename__ = 'ordertags_master'
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	first_tag_id = db.Column(db.Integer, db.ForeignKey('tags_master.id'))
	first_tag = db.relationship('Tags_master', foreign_keys='OrderTags_master.first_tag_id')
	last_tag_id = db.Column(db.Integer, db.ForeignKey('tags_master.id'))
	last_tag = db.relationship('Tags_master', foreign_keys='OrderTags_master.last_tag_id')

class Tags_semantic(db.Model):
	__tablename__ = 'tags_semantic'
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	tag = db.Column(db.Text, nullable=False)
	informations_tb = db.relationship('InformationTags_semantic', backref='tags_semantic', lazy='dynamic')


class OrderTags_semantic(db.Model):
	__tablename__ = 'ordertags_semantic'
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	first_tag_id = db.Column(db.Integer, db.ForeignKey('tags_semantic.id'))
	first_tag = db.relationship('Tags_semantic', foreign_keys='OrderTags_semantic.first_tag_id')
	last_tag_id = db.Column(db.Integer, db.ForeignKey('tags_semantic.id'))
	last_tag = db.relationship('Tags_semantic', foreign_keys='OrderTags_semantic.last_tag_id')


class InformationTags_master(db.Model):
	__tablename__ = 'informationtags_master'
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	tag_id = db.Column(db.Integer, db.ForeignKey('tags_master.id'))
	information_id = db.Column(db.Integer, db.ForeignKey('information.id'))


class InformationTags_semantic(db.Model):
	__tablename__ = 'informationtags_semantic'
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	tag_id = db.Column(db.Integer, db.ForeignKey('tags_semantic.id'))
	information_id = db.Column(db.Integer, db.ForeignKey('information.id'))


class Room(db.Model):
	__tablename__ = 'room'
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	name = db.Column(db.Text, nullable=False)
	location = db.Column(db.Text, nullable=False)
	messages_tb = db.relationship('Messages', backref='room', lazy='dynamic')
	characters_tb = db.relationship('RoomCharacter', backref='room', lazy='dynamic')


class RoomCharacter(db.Model):
	__tablename__ = 'roomcharacter'
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	room_id = db.Column(db.Integer, db.ForeignKey('room.id'))
	character_id = db.Column(db.Integer, db.ForeignKey('character.id'))


class Messages(db.Model):
	tablename__ = 'messages'
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	text = db.Column(db.Text, nullable=False)
	rooms_tb = db.Column(db.Integer, db.ForeignKey('room.id'))
	character_id = db.Column(db.Integer, db.ForeignKey('character.id'))
	datetime = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
