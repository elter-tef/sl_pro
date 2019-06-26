from flask import Blueprint, render_template
from ..db import db, User
module = Blueprint('test', __name__, url_prefix='/test')


@module.route('/')
def index():

    u = User(login='Benon')
    db.session.add(u)
    db.session.commit()
    #r = User.query.get(1)
    return 'hello {}'.format(3)
