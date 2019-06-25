from flask import Flask
from config import Config
from .db import db

def create():
	app = Flask(__name__)
	app.config.from_object(Config)
	db.init_app(app)
	
	import app.test as test
	app.register_blueprint(test.module)
	return app
