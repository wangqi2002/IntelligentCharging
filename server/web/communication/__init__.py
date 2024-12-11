from flask import Blueprint
communication = Blueprint('communication', __name__)
from . import views