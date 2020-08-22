# -*- coding: utf-8 -*-


class TestCreateApp(object):
    def test_factory_should_exists(self):
        import app
        assert hasattr(app, 'create_app')

    def test_should_create_a_new_flask_app(self):
        from flask.app import Flask
        import app
        new_app = app.create_app('testing')
        assert isinstance(new_app, Flask)
