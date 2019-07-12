from flask import Blueprint, request, jsonify, session
from ..db import db, User, Room, RoomCharacter, Tags_semantic, Messages, Character, Game, Knowledge, World, KnowledgeTags_semantic, Tags_master, KnowledgeTags_master, Item
from werkzeug.security import generate_password_hash
from ..func import js_dict
from flask_login import login_required, current_user
module = Blueprint('create', __name__, url_prefix='/create')


@module.route('/user', methods=['GET', 'POST']) #{"login" : str(), "password" : str(), "admin" : bool()}
def user():
    js_user = request.get_json()
    u = User(login = js_user['login'],
             password_hash = generate_password_hash(js_user['password']),
             admin = js_user['admin'])
    db.session.add(u)
    db.session.commit()
    return jsonify({ 'user': js_user['login']})


@login_required
@module.route('/game', methods=['GET', 'POST']) #{"world_id" : str(),"game" : str()}
def game():
    if not current_user.admin:
        return jsonify({"return" : "Access error"}), 403
    js_game = request.get_json()
    g = Game(world_id = js_game['world_id'], name = js_game['game'])
    db.session.add(g)
    db.session.commit()
    return jsonify({"return" : "Successfully"})


@login_required
@module.route('/world', methods=['GET', 'POST']) #{"world" : str()}
def world():
    if not current_user.admin:
        return jsonify({"return" : "Access error"}), 403
    js_world = request.get_json()
    w = World( id = js_world['world'])
    db.session.add(w)
    db.session.commit()
    return jsonify({"return" : "Successfully"})


@login_required
@module.route('/item', methods=['GET', 'POST']) #{"game_id" : int(),"name" : str(), "knowledge_id" : int()} //game_id == 0 -- общемировой предмет
def item():
    if not current_user.admin:
        return jsonify({"return" : "Access error"}), 403
    js_item = request.get_json()
    if not js_item['game_id']:
        game_id_ = 0
    else:
        game_id_ = session.get('current_game_id', 'not set')
    i = Item( game_id = game_id_, name = js_item['name'], knowledge_id = js_item['knowledge_id'])
    db.session.add(i)
    db.session.commit()
    return jsonify({"return": "Successfully", 'item_id' : i.id})


@login_required
@module.route('/character', methods=['GET', 'POST']) #{"game_id" : int(), "name" : str(), "quenta_id" : int()} //quenta_id являеться Knowledge
def character():
    if not current_user.admin:
        return jsonify({"return" : "Access error"}), 403
    js_character = request.get_json()
    c = Character(game_id = js_character['game_id'],name = js_character['name'], quenta_id = js_character['quenta_id'])
    db.session.add(c)
    db.session.commit()
    return jsonify({"return": "Successfully", "character_id" : c.id})

@login_required
@module.route('/knowledge', methods=['GET', 'POST']) #{"game_id" : int(), "concept" : str(), "text" : str(), "tags_semantic" : [str()], "tags_master" : [str()]} //game_id == 0 -- общемировые знания
def knowledge():
    js_knowledge = request.get_json()
    if not js_knowledge['game_id']:
        game_id_ = 0
    else:
        game_id_ = session.get('current_game_id', 'not set')
    k = Knowledge( game_id = game_id_, world_id = session.get('current_world_id', 'not set'),concept = js_knowledge['concept'], text = js_knowledge['text'])
    db.session.add(k)
    db.session.commit()
    for i in js_knowledge['tags_semantic']:
        t = Tags_semantic.query.filter(Tags_semantic.tag == i).first()
        if t is None:
            t = Tags_semantic(tag = i)
            db.session.add(t)
            db.session.commit()
        kt = KnowledgeTags_semantic(tag_id = t.id, knowledge_id = k.id)
        db.session.add(kt)
        db.session.commit()
    for i in js_knowledge['tags_master']:
        t = Tags_master.query.filter(Tags_master.tag == i).first()
        if t is None:
            t = Tags_master(tag = i)
            db.session.add(t)
            db.session.commit()
        kt = KnowledgeTags_master(tag_id = t.id, knowledge_id = k.id)
        db.session.add(kt)
        db.session.commit()
    return jsonify({"return" : "Successfully", "knowledge_id" : k.id})


@login_required
@module.route('/room', methods=['GET', 'POST']) #{"name" : str(),"description" : str(),"characters" : [{"character_id" : int(), "status" : str()}]}
def room():
    if not current_user.admin:
        return jsonify({"return" : "Access error"}), 403
    js_room = request.get_json()
    r = Room(name = js_room['name'], description = js_room['description'])
    db.session.add(r)
    db.session.commit()
    for i in js_room['characters']:
        rc = RoomCharacter(character_id = i['character_id'], room_id = r.id, status = i['status'])
        db.session.add(rc)
        db.session.commit()
    return jsonify({"return" : "Successfully", "room_id" : r.id})


@module.route('/json_out')
def json_out():
    u = User.query.filter(User.login == 'Ben').first()
    return ' -- {}'.format(js_dict(u))

@module.route('/json_in', methods=['GET', 'POST'])
def json_in():
    g = request.get_json()
    return str(g)
