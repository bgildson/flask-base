# -*- coding: utf-8 -*-

import pytest

from app.modules.todos.models import Todo


@pytest.fixture(scope='function')
def todos(db):
    """
    Create todo fixtures
    """
    db.session.query(Todo).delete()

    todos = [
        {
            'description': 'brush teeth',
            'done': True,
        },
        {
            'description': 'take a shower',
            'done': False,
        },
    ]

    for todo in todos:
        db.session.add(Todo(**todo))

    db.session.commit()

    return db.session.query(Todo).all()
