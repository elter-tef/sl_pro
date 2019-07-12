from flask import Blueprint, jsonify, request
from ..db import db, World, Game, Room, RoomCharacter, KnowledgeCharacter
from flask_login import login_required, current_user
module = Blueprint('remove', __name__, url_prefix='/remove')

@login_required
@module.route('/chrfromroom', methods=['GET', 'POST']) #{"room_id" : int(), "character_id" : int()}
def chrfromroom():
    if not current_user.admin:
        return jsonify({"return" : "Access error"}), 403
    js_room = request.get_json()
    rc = Room.query.get(js_room['room_id']).characters_tb.filter(RoomCharacter.character_id == js_room['character_id']).first()
    db.session.delete(rc)
    db.session.commit()
    return jsonify({"return": "Successfully"})