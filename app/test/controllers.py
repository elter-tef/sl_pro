from flask import Blueprint, render_template
from ..db import db, User
module = Blueprint('test', __name__, url_prefix='/test')


@module.route('/')
def index():
    u = User( login='Ben')
    db.session.add(u)
    db.session.commit()
    u = User(login='Sol')
    db.session.add(u)
    db.session.commit()
    u = User(login='Benon')
    db.session.add(u)
    db.session.commit()
    r = User.query.filter_by(login='Benon').first()
    return 'hello {}'.format(r.id)
