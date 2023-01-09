from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config.from_object("project.config.Config")

db = SQLAlchemy(app)

from project.container import Container
from project.ui.routes.user import get_user_route

app.register_blueprint(get_user_route.blueprint, url_prefix="/user")

container = Container()

app.container = container

container.wire(modules=[
    __name__,
    get_user_route
])







