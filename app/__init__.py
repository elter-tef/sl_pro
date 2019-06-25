from flask import Flask
from config import Config
from .db import db, User

def create():
	app = Flask(__name__)
	app.config.from_object(Config)
	u = User()
	db.session.add(u)
	db.session.commit()
	db.init_app(app)
	
	#import app.main as main
	#app.register_blueprint(main.module)
	return app
