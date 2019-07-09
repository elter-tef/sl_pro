from flask import Blueprint
from ..db import db, User
from flask_login import  LoginManager, current_user, login_user, logout_user
from ..func import js_dict
from flask import request, jsonify
from werkzeug.security import check_password_hash
import json
module = Blueprint('login', __name__, url_prefix='/login')
lm = LoginManager()

@lm.user_loader
def load_user(id):
    return User.query.get(int(id))


@module.route('/', methods=['GET', 'POST'])
def login(): #{"login" : str(), "password" : str(), "remember" : bool()}
    js_user = request.get_json()
    if current_user.is_authenticated:
        return jsonify({"return" : "Is authenticated"})
    user = User.query.filter(User.login == js_user['login']).first()
    if user is None or not check_password_hash(user.password_hash   , js_user['password']):
        return jsonify({"return" : "Invalid username or password"})
    login_user(user, js_user["remember"])
    return jsonify({"return" : "Successfully"})

@module.route('/logout', methods=['GET', 'POST'])
def logout(): #{}
    logout_user()
    return jsonify({"return" : "Successfully"})

@module.route('/json_out')
def json_out():
    u = User.query.filter(User.login == 'Ben').first()
    return ' -- {}'.format(js_dict(u))

@module.route('/json_in', methods=['GET', 'POST'])
def json_in():
    g = request.get_json()
    return str(g)
