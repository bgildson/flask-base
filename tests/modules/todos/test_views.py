# -*- coding: utf-8 -*-

from flask import url_for


class TestTodos(object):
    def test_list_all(self, app, client, todos):
        with app.test_request_context():
            res = client.get(url_for('todos.index'))
            assert res.status_code == 200

            items = res.get_json()

            assert len(items) == len(todos)

            for item in items:
                for todo in todos:
                    if item['description'] == todo.description and \
                       item['done'] == todo.done:
                        assert True
                        break
                else:
                    assert False
