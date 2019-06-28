from flask import Blueprint, render_template
from ..db import db, User, Address
module = Blueprint('test', __name__, url_prefix='/test')


@module.route('/')
def index():
    u = User( login='Ben')
    db.session.add(u)
    db.session.commit()
    u = Address(email='spot',user_id=User.query.filter_by(login='Ben').first().id)
    db.session.add(u)
    db.session.commit()
    u = Address(email='iopr', user_id=User.query.filter_by(login='Ben').first().id)
    db.session.add(u)
    db.session.commit()
    u = Address(email='got', user_id=User.query.filter_by(login='Ben').first().id)
    db.session.add(u)
    db.session.commit()
    #r = User.query.filter_by(login='Ben').first()
    r = Address.query.filter_by(user_id=User.query.filter_by(login='Ben').first().id).all()
    return 'hello {}'.format(r)
