# -*- coding: utf-8 -*-

from app.modules.todos.models import Todo


class TestTodo(object):
    def test_as_dict_for_every_col(self):
        todo = Todo(description='my description', done=True)

        expected_keys = ('id', 'description', 'done', 'created_at',)
        dict_keys = todo.as_dict().keys()

        assert len(dict_keys) == len(expected_keys)

        for key in expected_keys:
            assert key in dict_keys
