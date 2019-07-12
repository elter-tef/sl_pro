from flask import Blueprint, jsonify, request
from ..db import db, Character, User, ItemCharacter, KnowledgeCharacter, Room, RoomCharacter
from flask_login import login_required, current_user
module = Blueprint('add', __name__, url_prefix='/add')

@login_required
@module.route('/usercharacter', methods=['GET', 'POST']) #{"user_id" : int(), "character_id" : int()}
def usercharacter():
    json = request.get_json()
    if not current_user.admin:
        return jsonify({"return" : "Access error"}), 403
    c = Character.query.get(json['character_id'])
    c.user_id = json['user_id']
    db.session.add(c)
    db.session.commit()
    return jsonify({"return": "Successfully"})


@login_required
@module.route('/quentacharacter', methods=['GET', 'POST']) #{"quenta_id" : int(), "character_id" : int()}
def quentacharacter():
    json = request.get_json()
    if not current_user.admin:
        return jsonify({"return" : "Access error"}), 403
    c = Character.query.get(json['character_id'])
    c.quenta_id = json['quenta_id']
    db.session.add(c)
    db.session.commit()
    return jsonify({"return": "Successfully"})


@login_required
@module.route('/itemcharacter', methods=['GET', 'POST']) #{"item_id" : int(), "character_id" : int(), "item_number" : int()}
def itemcharacter():
    json = request.get_json()
    if not current_user.admin:
        return jsonify({"return" : "Access error"}), 403
    ic = ItemCharacter(item_id = json['item_id'], character_id = json['character_id'], number = json['item_number'])
    db.session.add(ic)
    db.session.commit()
    return jsonify({"return": "Successfully"})


@login_required
@module.route('/knowledgecharacter', methods=['GET', 'POST']) #{"knowledge_id" : int(), "character_id" : int()}
def knowledgecharacter():
    json = request.get_json()
    if not current_user.admin:
        return jsonify({"return" : "Access error"}), 403
    kc = KnowledgeCharacter(knowledge_id = json['knowledge_id'], character_id = json['character_id'])
    db.session.add(kc)
    db.session.commit()
    return jsonify({"return": "Successfully"})


@login_required
@module.route('/chrtoroom', methods = ['GET', 'POST']) #{"room_id" : int(), "characters" : [{"character_id" : int(), "status" : str()}]}
def chrtoroom():
    if not current_user.admin:
        return jsonify({"return" : "Access error"}), 403
    js_room = request.get_json()
    r = Room.query.get(js_room['room_id'])
    for i in js_room['characters']:
        rc = RoomCharacter(character_id = i['character_id'], room_id = r.id, status = i['status'])
        db.session.add(rc)
        db.session.commit()
    return jsonify({"return": "Successfully", "room_id": r.id})