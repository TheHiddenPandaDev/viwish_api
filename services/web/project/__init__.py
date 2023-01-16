from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config.from_object("project.config.Config")

db = SQLAlchemy(app)

from project.container import Container
from project.ui.routes.user import get_user_route
from project.ui.routes.log import get_log_route
from project.ui.routes.log import create_log_route

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







