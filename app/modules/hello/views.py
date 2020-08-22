# -*- coding: utf-8 -*-

from flask import Blueprint
from flask.templating import render_template


bp = Blueprint('hello',
               __name__,
               url_prefix='/hello',
               template_folder='templates',
               static_folder='static',
               static_url_path='/static')


@bp.route('/')
def index():
    return render_template('layouts/index.html')
