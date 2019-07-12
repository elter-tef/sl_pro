from flask import Blueprint, jsonify, request
from ..db import db, World, Game, Room, RoomCharacter
from flask_login import login_required, current_user
module = Blueprint('change', __name__, url_prefix='/change')

@login_required
@module.route('/chrstatus', methods=['GET', 'POST']) #{"room_id" : int(), "characters" : [{"character_id" : int(), "status" : str()}]}
def chrfromroom():
    if not current_user.admin:
        return jsonify({"return" : "Access error"}), 403
    js_room = request.get_json()
    rc = Room.query.get(js_room['room_id']).characters_tb.filter(RoomCharacter.character_id == js_room['character_id']).first()
    rc.status = js_room['status']
    db.session.add(rc)
    db.session.commit()
    return jsonify({"return": "Successfully"})