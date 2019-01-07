from flask import Blueprint

main = Blueprint('main', __name__, template_folder='templates')
from app.catalog import routes, models  # to avoid circular imports
