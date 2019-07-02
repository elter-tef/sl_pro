from flask import Blueprint, render_template
from ..db import db, User, Item, ItemUser, Address
module = Blueprint('test', __name__, url_prefix='/test')


@module.route('/')
def index():
    u = User(login='Ben')
    db.session.add(u)
    db.session.commit()
    u = User.query.filter(login='Ben')
    u.address_tb = [Address(email = 'qwerty')]
    db.session.add(u)
    db.session.commit()
    u = User.query.filter_by(login='Ben').first().address_tb.all()
    s = []
    for i in u:
        s.append(i.email)
    return 'User {} has {}'.format(1, s)

@module.route('/a')
def aaa():
    u = User( login='Ben')
    db.session.add(u)
    db.session.commit()
    u = User(login='Sasha')
    db.session.add(u)
    db.session.commit()
    u = Item(name='wood')
    db.session.add(u)
    db.session.commit()
    u = Item(name='glass')
    db.session.add(u)
    db.session.commit()
    u = Item(name='sand')
    db.session.add(u)
    db.session.commit()
    u = ItemUser(user_id=User.query.filter_by(login='Ben').first().id,
                 item_id=Item.query.filter_by(name='glass').first().id)
    db.session.add(u)
    db.session.commit()
    u = ItemUser(user_id=User.query.filter_by(login='Sasha').first().id,
                 item_id=Item.query.filter_by(name='wood').first().id)
    db.session.add(u)
    db.session.commit()
    #r = User.query.filter_by(login='Ben').first()
    user = 'Ben'
    g = User.query.filter(User.login == 'Ben').first().items_user.filter(Item.name == 'glass').first()
    r = User.query.filter(User.login == user).first().items_user
    items = []
    for i in r:
        items.append(Item.query.get(i.item_id).name)
    return 'User {} has {}'.format(user,items)
