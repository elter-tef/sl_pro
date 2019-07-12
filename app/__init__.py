from flask import Flask
from config import Config
from app.db import db
from app.login import lm
from app.func import degrade
def create():
	app = Flask(__name__)
	app.config.from_object(Config)
	db.init_app(app)
	lm.init_app(app)
	degrade()
	with app.test_request_context():
		db.create_all()
	import app.test as test
	app.register_blueprint(test.module)
	import app.create as create
	app.register_blueprint(create.module)
	import app.login as login
	app.register_blueprint(login.module)
	import app.index as index
	app.register_blueprint(index.module)
	import app.get as get
	app.register_blueprint(get.module)
	import app.add as add
	app.register_blueprint(add.module)
	import app.change as change
	app.register_blueprint(change.module)
	import app.remove as remove
	app.register_blueprint(remove.module)
	import app.post as post
	app.register_blueprint(post.module)
	return app
