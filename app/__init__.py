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
	return app
