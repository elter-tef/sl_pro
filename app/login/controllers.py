from flask import Blueprint, session
from ..db import db, User, Character
from flask_login import  LoginManager, current_user, login_user, logout_user, login_required
from ..func import js_dict
from flask import request, jsonify
from werkzeug.security import check_password_hash
import json
module = Blueprint('login', __name__, url_prefix='/login')
lm = LoginManager()
lm.login_view = 'login'

@lm.user_loader
def load_user(id):
    return User.query.get(int(id))


@module.route('/', methods=['GET', 'POST']) #{"login" : str(), "password" : str(), "remember" : bool()}
def login():
    js_user = request.get_json()
    if current_user.is_authenticated:
        return jsonify({"return" : "Is authenticated"})
    user = User.query.filter(User.login == js_user['login']).first()
    if user is None or not check_password_hash(user.password_hash   , js_user['password']):
        return jsonify({"return" : "Invalid username or password"}), 404
    login_user(user, js_user["remember"])
    return jsonify({"return" : "Successfully", "admin" : current_user.admin})


@login_required
@module.route('/character', methods=['GET', 'POST']) #{"character_id" : int(), "game_id : int()", "world_id" : str()} //сharacter_id == 0 -- вход для мастерского персонажа
def character():
    js_character = request.get_json()
    if js_character['character_id'] == 0:
        if not current_user.admin:
            return jsonify({"return": "Access error"}), 403
        session['current_character_id'] = 0
        return jsonify({"return": "Successfully", "admin" : 1})
    else:
        session['current_character_id'] = js_character['character_id']
    session['current_game_id'] = js_character['game_id']
    session['current_world_id'] = js_character['world_id']
    return jsonify({"return": "Successfully"})


@module.route('/logout', methods=['GET', 'POST']) #{}
def logout():
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
