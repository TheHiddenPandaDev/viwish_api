from flask.cli import FlaskGroup

from project import app
from project import db
from project.domain.user.user import User

cli = FlaskGroup(app)

@cli.command("create_db")
def create_db():
    db.drop_all()
    db.create_all()
    db.session.commit()

    # Seed DB
    db.session.add(User(email="michael@mherman.org"))
    db.session.commit()

if __name__ == "__main__":
    cli()
