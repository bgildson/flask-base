# -*- coding: utf-8 -*-

from flask import Blueprint, jsonify

from .models import Todo


bp = Blueprint('todos', __name__, url_prefix='/todos')


@bp.route('/')
def index():
    try:
        todos = Todo.query.all()
        todos_dict = [todo.as_dict() for todo in todos]
        return jsonify(todos_dict)
    except Exception:
        return jsonify({'message': 'could not get all todos'})
