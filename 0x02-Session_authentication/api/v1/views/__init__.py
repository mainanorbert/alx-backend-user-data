#!/usr/bin/env python3
""" DocDocDocDocDocDoc
"""
# from flask import Blueprint
# from flask import Blueprint
from markupsafe import Markup
from flask import Blueprint, jsonify, request, abort


app_views = Blueprint("app_views", __name__, url_prefix="/api/v1")

from api.v1.views.index import *
from api.v1.views.users import *

User.load_from_file()
