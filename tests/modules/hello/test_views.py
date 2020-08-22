# -*- coding: utf-8 -*-

from flask.app import Flask, url_for
from flask.testing import FlaskClient


def test_hello_responds_right_content(app: Flask, client: FlaskClient):
    with app.test_request_context():
        res = client.get(url_for('hello.index'))
        assert res.status_code == 200
        assert b'Hello world' in res.data
