# -*- coding: utf-8 -*-

from . import hello
from . import todos


def init_app(app):
    hello.init_app(app)
    todos.init_app(app)
