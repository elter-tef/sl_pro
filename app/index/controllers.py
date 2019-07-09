from flask import Blueprint, g, session, redirect, url_for
from ..db import db, User, Tags_semantic, OrderTags_semantic, Messages, Character, Game, Knowledge
from flask_login import  LoginManager, current_user
from ..func import js_dict
from flask import request, jsonify
from werkzeug.security import check_password_hash
import json
module = Blueprint('create', __name__, url_prefix='/create')
lm = LoginManager()

@lm.user_loader
def load_user(id):
    return User.query.get(int(id))


@module.route('/')
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
@module.route('/json_out')
def json_out():
    u = User.query.filter(User.login == 'Ben').first()
    return ' -- {}'.format(js_dict(u))

@module.route('/json_in', methods=['GET', 'POST'])
def json_in():
    g = request.get_json()
    return str(g)
