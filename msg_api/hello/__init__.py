from .controller.hello import HelloController
from flask import Blueprint

hello_bp = Blueprint("hello", __name__, url_prefix="/api/hello")

hello_bp.add_url_rule("/", view_func=HelloController.as_view("hello"))