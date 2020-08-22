# -*- coding: utf-8 -*-
"""
Generate a central db instance
"""

from flask_sqlalchemy import SQLAlchemy


db: SQLAlchemy = SQLAlchemy()
