from flask import Blueprint, jsonify, request
from ..db import db, World, Game, Messages
from flask_login import login_required, current_user
module = Blueprint('post', __name__, url_prefix='/post')

@login_required
@module.route('/messages', methods=['GET', 'POST']) #{"room_id" : int(), "character_id" : int(), "text" : str()}
def messages():
    json = request.get_json()
    if not current_user.admin:
        return jsonify({"return": "Access error"}), 403
    m = Messages(room_id = json['room_id'], character_id = json['character_id'], text = json['text'])
    db.session.add(m)
    db.session.commit()
    return jsonify({"return": "Successfully", "messages_id" : m.id})