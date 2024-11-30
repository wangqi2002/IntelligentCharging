from flask import Blueprint
station = Blueprint('station', __name__)
from . import views