from flask import Blueprint, render_template, g, session
from ..db import db, User, Tags_semantic, OrderTags_semantic, Messages, Character, Game, Knowledge, RoomCharacter
from ..func import js_dict
from flask import request, jsonify
from flask_login import   current_user
import json
module = Blueprint('test', __name__, url_prefix='/test')

@module.route('/one')
def one():
    s = ['{} {} {}'.format(i.character_id, i.room_id, i.status) for i in RoomCharacter.query.all()]
    return '{}'.format(s)

@module.route('/two')
def two():
    u = User.query.all()
    s = []
    for i in u:
        s.append(str(i.login) + ' ' +str(i.id))
    return '{}'.format(s)

@module.route('/json_out')
def json_out():
    u = User.query.filter(User.login == 'Ben').first()
    return ' -- {}'.format(js_dict(u))

@module.route('/json_in', methods=['GET', 'POST'])
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


@module.route('/game')
def game():
    g = Game(name = 'first')
    k = Knowledge(concept = 'a', text = 'b')
    db.session.add(g)
    db.session.add(k)
    db.session.commit()
    k2 = Knowledge(concept='a', text='n', game_id = Game.query.filter(Game.name == 'first').first().id)
    db.session.add(k2)
    db.session.commit()
    #
    return 'as {}'.format( Knowledge.query.filter(Knowledge.game_id == 1).first().text  )

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
    u = OrderTags_semantic(first_tag = Tags_semantic.query.filter_by(tag = 'sql').first(),
                         last_tag = Tags_semantic.query.filter_by(tag = 'horse').first())

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