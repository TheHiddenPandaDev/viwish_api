from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy

from project.domain.viwish_exception import ViWishException

app = Flask(__name__)
app.config.from_object("project.config.Config")

db = SQLAlchemy(app)

from project.container import Container
from project.ui.routes.user import get_user_route
from project.ui.routes.log import get_log_route
from project.ui.routes.log import create_log_route

@app.errorhandler(Exception)
def handle_error(e):
    code = 500
    if hasattr(e, 'get_response') and hasattr(e, 'code'):
        return e.get_response(), e.code
    return jsonify(error=str(e)), code

app.register_blueprint(get_log_route.blueprint, url_prefix="/log")
app.register_blueprint(create_log_route.blueprint, url_prefix="/log")
app.register_blueprint(get_user_route.blueprint, url_prefix="/user")

container = Container()

app.container = container

container.wire(modules=[
    __name__,
    get_log_route,
    create_log_route,
    get_user_route,
])







