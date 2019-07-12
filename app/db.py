from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from datetime import datetime
db = SQLAlchemy()
class World(db.Model):
	__tablename__ = 'world'
	id = db.Column(db.Text, primary_key=True)
	game_tb = db.relationship('Game', backref='world', lazy='dynamic')
	knowledge_tb = db.relationship('Knowledge', backref='world', lazy='dynamic')

class Game(db.Model):
	__tablename__ = 'game'
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	world_id = db.Column(db.Text, db.ForeignKey('world.id'))
	name = db.Column(db.Text, nullable=False)
	character_tb = db.relationship('Character', backref='game', lazy='dynamic')
	room_tb = db.relationship('Room', backref='game', lazy='dynamic')
	item_tb = db.relationship('Item', backref='game', lazy='dynamic')
	knowledge_tb = db.relationship('Knowledge', backref='game', lazy='dynamic')


class User(UserMixin, db.Model):
	__tablename__ = 'user'
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	admin = db.Column(db.Boolean, default=False)
	login =  db.Column(db.Text, nullable=False)
	password_hash = db.Column(db.Text, nullable=False)
	character_tb = db.relationship('Character', backref='user', foreign_keys = 'Character.user_id', lazy='dynamic')


class Character(db.Model):
	__tablename__ = 'character'
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	game_id = db.Column(db.Integer, db.ForeignKey('game.id'))
	name = db.Column(db.Text, nullable=False)
	quenta_id = db.Column(db.Integer, db.ForeignKey('knowledge.id'))
	user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
	game_tb = db.relationship('Game', lazy='joined')
	item_tb = db.relationship('ItemCharacter', backref='character',lazy='dynamic')
	knowledges_tb = db.relationship('KnowledgeCharacter', backref='character', lazy='dynamic')
	room_tb = db.relationship('RoomCharacter', backref='character', lazy='dynamic')
	messages_tb = db.relationship('Messages', backref='character', lazy='dynamic')


class Item(db.Model):
	__tablename__ = 'item'
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	game_id =  db.Column(db.Integer, db.ForeignKey('game.id'))
	knowledge_id = db.Column(db.Integer, db.ForeignKey('knowledge.id'))
	name = db.Column(db.Text, nullable=False)
	characters_tb = db.relationship('ItemCharacter', backref='item', lazy='dynamic')



class Knowledge(db.Model):
	__tablename__ = 'knowledge'
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	game_id = db.Column(db.Integer, db.ForeignKey('game.id'), default=0)
	world_id = db.Column(db.Text, db.ForeignKey('world.id'))
	concept = db.Column(db.Text, nullable=False)
	text = db.Column(db.Text, nullable=False)
	characters_tb = db.relationship('KnowledgeCharacter', backref='knowledges', lazy='dynamic')
	items_tb = db.relationship('Item', backref='knowledges', lazy='dynamic')
	tags_master_tb = db.relationship('KnowledgeTags_master', backref='knowledge', lazy='dynamic')
	tags_semantic_tb = db.relationship('KnowledgeTags_semantic', backref='knowledge', lazy='dynamic')


class KnowledgeCharacter(db.Model):
	__tablename__ = 'knowledge_character'
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	character_id = db.Column(db.Integer, db.ForeignKey('character.id'))
	knowledge_id = db.Column(db.Integer, db.ForeignKey('knowledge.id'))


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
	knowledges_tb = db.relationship('KnowledgeTags_master', backref='tags_master', lazy='dynamic')
	first_tag_tb = db.relationship('OrderTags_master', foreign_keys='OrderTags_master.first_tag_id', lazy='joined')
	last_tag_tb = db.relationship('OrderTags_master', foreign_keys='OrderTags_master.last_tag_id', lazy='joined')


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
	knowledges_tb = db.relationship('KnowledgeTags_semantic', backref='tags_semantic', lazy='dynamic')
	first_tag_tb = db.relationship('OrderTags_semantic', foreign_keys='OrderTags_semantic.first_tag_id', lazy='joined')
	last_tag_tb = db.relationship('OrderTags_semantic', foreign_keys='OrderTags_semantic.last_tag_id', lazy='joined')


class OrderTags_semantic(db.Model):
	__tablename__ = 'ordertags_semantic'
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	first_tag_id = db.Column(db.Integer, db.ForeignKey('tags_semantic.id'))
	first_tag = db.relationship('Tags_semantic', foreign_keys='OrderTags_semantic.first_tag_id', lazy='joined')
	last_tag_id = db.Column(db.Integer, db.ForeignKey('tags_semantic.id'))
	last_tag = db.relationship('Tags_semantic', foreign_keys='OrderTags_semantic.last_tag_id', lazy='joined')


class KnowledgeTags_master(db.Model):
	__tablename__ = 'knowledgetags_master'
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	tag_id = db.Column(db.Integer, db.ForeignKey('tags_master.id'))
	knowledge_id = db.Column(db.Integer, db.ForeignKey('knowledge.id'))


class KnowledgeTags_semantic(db.Model):
	__tablename__ = 'knowledgetags_semantic'
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	tag_id = db.Column(db.Integer, db.ForeignKey('tags_semantic.id'))
	knowledge_id = db.Column(db.Integer, db.ForeignKey('knowledge.id'))


class Room(db.Model):
	__tablename__ = 'room'
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	game_id = db.Column(db.Integer, db.ForeignKey('game.id'))
	name = db.Column(db.Text, nullable=False)
	description = db.Column(db.Text, nullable=False)
	messages_tb = db.relationship('Messages', backref='room', lazy='dynamic')
	characters_tb = db.relationship('RoomCharacter', backref='room', lazy='dynamic')


class RoomCharacter(db.Model):
	__tablename__ = 'roomcharacter'
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	nvdm = db.Column(db.Boolean)
	status = db.Column(db.Text, nullable=False)
	room_id = db.Column(db.Integer, db.ForeignKey('room.id'))
	character_id = db.Column(db.Integer, db.ForeignKey('character.id'))
	#locations_tb = db.relationship('LocationRoomCharacter', backref='roomcharacter', lazy='dynamic')





class Messages(db.Model):
	tablename__ = 'messages'
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	text = db.Column(db.Text, nullable=False)
	room_id = db.Column(db.Integer, db.ForeignKey('room.id'))
	character_id = db.Column(db.Integer, db.ForeignKey('character.id'))
	datetime = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
