from flask import Blueprint
gun = Blueprint('gun', __name__)
from . import views