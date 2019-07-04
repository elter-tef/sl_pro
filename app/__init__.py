from flask import Flask
from config import Config
from .db import db
from .func import degrade
def create():
	app = Flask(__name__)
	app.config.from_object(Config)
	db.init_app(app)
	degrade()
	with app.test_request_context():
		db.create_all()
	import app.test as test
	app.register_blueprint(test.module)
	return app
