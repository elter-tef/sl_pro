from flask import Blueprint, render_template
from ..db import db, User, Tags_semantic, OrderTags_semantic, Messages, Character
from ..func import js_dict
from flask import request, jsonify
import json
module = Blueprint('test', __name__, url_prefix='/test')

@module.route('/json_out')
def json_out():
    u = User.query.filter(User.login == 'Ben').first()
    return ' -- {}'.format(js_dict(u))

@module.route('/json_in')
def json_in():
    g = request.get_json()
    return str(g)
@module.route('/')
def index():
    u = User(login = 'Ben')
    db.session.add(u)
    db.session.commit()
    g = User.query.filter_by(login = 'Ben').first()
    u = Character(name='Фоллен', user_id = g.id)
    db.session.add(u)
    db.session.commit()
    return '{}'.format(Character.query.filter_by(name='Фоллен').first().id)
    #u = Character()
    #u = Messages(text = 'now', character_id,)
    #db.session.add(u)
    #db.session.commit()


@module.route('/tag')
def tag():
    u = Tags_semantic( tag = 'sql')
    db.session.add(u)
    db.session.commit()
    u = Tags_semantic( tag = 'horse')
    db.session.add(u)
    db.session.commit()
    u = Tags_semantic( tag = 'ослик')
    db.session.add(u)
    db.session.commit()
    u = OrderTags_semantic(first_tag_id = Tags_semantic.query.filter_by(tag = 'sql').first().id,
                         last_tag_id = Tags_semantic.query.filter_by(tag = 'horse').first().id)
    db.session.add(u)
    db.session.commit()
    u = OrderTags_semantic(first_tag_id=Tags_semantic.query.filter_by(tag='sql').first().id,
                         last_tag_id=Tags_semantic.query.filter_by(tag='ослик').first().id)
    db.session.add(u)
    db.session.commit()
    find_tag = 'sql'
    s,f = [],[]
    for i in OrderTags_semantic.query.filter_by(first_tag_id = Tags_semantic.query.filter_by( tag = 'sql').first().id).all():
        s.append(i.last_tag_id)
    for i in s:
        f.append(Tags_semantic.query.get(i).tag)
    return 'User {}'.format(f)