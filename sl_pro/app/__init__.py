from flask import Flask
from config import Config
from .db import db
def create():
	app = Flask(__name__)
	app.config.from_object(Config)
	db.init_app(app)
	import app.main as main
	app.register_blueprint(main.module)
	return app
app = create()
