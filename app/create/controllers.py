from flask import Blueprint, render_template, g, session
from ..db import db, User, Tags_semantic, OrderTags_semantic, Messages, Character, Game, Knowledge
from werkzeug.security import generate_password_hash
from ..func import js_dict
from flask import request, jsonify
module = Blueprint('create', __name__, url_prefix='/create')

@module.route('/user', methods=['GET', 'POST']) #{"login" : str(), "password" : str(), "admin" : bool()}
def user():
    js_user = request.get_json()
    u = User(login =js_user['login'], password_hash = generate_password_hash(js_user['password']), admin = js_user['admin'])
    db.session.add(u)
    db.session.commit()
    return jsonify({ 'user': js_user['login']})

@module.route('/json_out')
def json_out():
    u = User.query.filter(User.login == 'Ben').first()
    return ' -- {}'.format(js_dict(u))

@module.route('/json_in', methods=['GET', 'POST'])
def json_in():
    g = request.get_json()
    return str(g)
