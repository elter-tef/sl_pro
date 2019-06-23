from flask import Blueprint, render_template

module = Blueprint('public', __name__, url_prefix='/public')


@module.route('/low')
def index():
    return 'hello'
