from flask import Flask
import os
from app.models import db
from app.serializers import ma
from app.views import routes
from flask_migrate import Migrate

app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))

# db settings
DB_PASSWORD = os.environ["MYSQL_PASSWORD"]
DB_NAME = os.environ["MYSQL_DATABASE"]
DB_USER = os.environ["MYSQL_USER"]
DB_PORT = os.environ["MYSQL_PORT"]
app.config["SQLALCHEMY_DATABASE_URI"] = f'mysql+pymysql://{DB_USER}:{DB_PASSWORD}@localhost:{DB_PORT}/{DB_NAME}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
migrate = Migrate(app, db)

ma.init_app(app)

# app routing
app.register_blueprint(routes)
