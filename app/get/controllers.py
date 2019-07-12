from flask import Blueprint, jsonify, request
from ..db import db, World, Game, Messages, Knowledge, Character, KnowledgeCharacter, Tags_master, Tags_semantic, Item, ItemCharacter
from flask_login import login_required, current_user
from sqlalchemy import  desc
module = Blueprint('get', __name__, url_prefix='/get')

@login_required
@module.route('/logincharacter', methods=['GET', 'POST'])
def logincharacter():
    js_menu = dict()
    js_menu['worlds'] = [{"word_id" : i.id, 'games' : [{'game_name' : a.name, 'game_id' : a.id, 'characters' : [{'character_name' : o.name, 'character_id' : o.id} for o in current_user.character_tb.all()]} for a in World.query.get(i.id).game_tb.all()] } for i in World.query.all()]
    return jsonify(js_menu)

@login_required
@module.route('/messages', methods=['GET', 'POST'])
def messages():
    js_dict = dict()
    js_dict["messages"] = [ {"character_id" : i.character_id, "text" : i.text} for i in Messages.query.order_by(desc(Messages.datetime)).limit(10).all() ]
    return jsonify(js_dict)


@login_required
@module.route('/knowledge', methods=['GET', 'POST']) #{"knowledge_id" : int(), "character_id" : int()}
def knowledge():
    json = request.get_json()
    kc = Character.query.get(json['character_id']).knowledges_tb.filter(
        KnowledgeCharacter.knowledge_id == json['knowledge_id']).first()
    if  kc is None:
        return jsonify({"return": "Not found"}), 404
    js_knowledge = dict()
    k = Knowledge.query.get(kc.knowledge_id)
    js_knowledge["game_id"] = k.game_id
    js_knowledge["concept"] = k.concept
    js_knowledge["text"] = k.text
    js_knowledge["tags_semantic"] = [Tags_semantic.query.get(i.tag_id).tag for i in k.tags_semantic_tb.all()]
    js_knowledge["tags_master"] = [Tags_master.query.get(i.tag_id).tag for i in k.tags_master_tb.all()]
    return jsonify(js_knowledge)


@login_required
@module.route('/item', methods=['GET', 'POST']) #{"item_id" : int(), "character_id" : int()}
def item():
    json = request.get_json()
    ic = Character.query.get(json['character_id']).item_tb.filter(
        ItemCharacter.item_id == json['item_id']).first()
    if  ic is None:
        return jsonify({"return": "Not found"}), 404
    js_item = dict()
    i = Item.query.get(ic.item_id)
    js_item["game_id"] = i.game_id
    js_item["name"] = i.name
    js_item["knowledge_id"] = i.knowledge_id
    js_item["item_number"] = ic.number
    return jsonify(js_item)

@login_required
@module.route('/character', methods=['GET', 'POST']) #{"character_id" : int()}
def character():
    json = request.get_json()
    c = Character.query.get(json['character_id'])
    if c is None:
        return jsonify({"return": "Not found"}), 404
    js_character = dict()
    js_character["game_id"] = c.game_id
    js_character["name"] = c.name
    js_character["quenta_id"] = c.quenta_id
    js_character["user_id"] = c.user_id
    return jsonify(js_character)