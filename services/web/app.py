from flask import Flask
from dependency_injection import DI
from project.ui.routes.user import get_user_route

app = Flask(__name__)
app.config.from_object("project.config.Config")
app.register_blueprint(get_user_route.blueprint, url_prefix="/user")

if __name__ == "__main__":
    di = DI()
    di.wire(modules=[
        get_user_route
    ])

    app.run(debug=True)