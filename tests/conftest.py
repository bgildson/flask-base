# -*- coding: utf-8 -*-

import pytest

from app import create_app
from app.utils.db import db as _db


@pytest.fixture(scope='session')
def app():
    """
    Creates an app injectable in session level
    """
    return create_app('testing')


@pytest.fixture(scope='session')
def client(app):
    """
    Creates a http client injectable in session level
    """
    return app.test_client()


@pytest.fixture(scope='session', autouse=True)
def db(app):
    """
    Creates the tests db injectable in session level
    """
    with app.app_context():
        _db.create_all()

        yield _db

        _db.drop_all()


# @pytest.yield_fixture(scope='function')
# def session(db):
#     db.session.begin_nested()

#     yield db.session

#     db.session.rollback()
