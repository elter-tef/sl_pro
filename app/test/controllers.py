from flask import Blueprint, render_template
from ..db import db, User
module = Blueprint('test', __name__, url_prefix='/test')


@module.route('/')
def index():
    u = User()
    db.session.add(u)
    db.session.commit()
    return 'hello {}'.format(u.id)
