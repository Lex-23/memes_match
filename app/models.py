from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    city = db.Column(db.String(50))
    info = db.Column(db.String(300))
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))

    def __init__(self, name, city, info, email, password):
        self.name = name
        self.city = city
        self.info = info
        self.email = email
        self.password = password


class Meme(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(300))
    filename = db.Column(db.String(100))
    data = db.Column(db.LargeBinary)
    original_url = db.Column(db.String(300), unique=True)
    description = db.Column(db.String(300), default=None)

    def __init__(self, name, filename, data, original_url, description):
        self.name = name
        self.filename = filename
        self.data = data
        self.original_url = original_url
        self.description = description
