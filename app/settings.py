import os

import connexion
from flask_migrate import Migrate

from app.models import db, ma

basedir = os.path.abspath(os.path.dirname(__file__))

# app = Flask(__name__)
connex_app = connexion.App(__name__, specification_dir=basedir)
connex_app.add_api("swagger.yml")

app = connex_app.app
app.app_context().push()


# db settings
DB_PASSWORD = os.environ["MYSQL_PASSWORD"]
DB_NAME = os.environ["MYSQL_DATABASE"]
DB_USER = os.environ["MYSQL_USER"]
DB_PORT = os.environ["MYSQL_PORT"]
app.config[
    "SQLALCHEMY_DATABASE_URI"
] = f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@localhost:{DB_PORT}/{DB_NAME}"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SQLALCHEMY_ECHO"] = True

db.init_app(app)

ma.init_app(app)

migrate = Migrate(app, db)
