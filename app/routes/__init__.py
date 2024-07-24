from flask import Blueprint

app_routes = Blueprint('routes', __name__,url_prefix="/")

from . import routes