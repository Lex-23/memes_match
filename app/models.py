from flask_sqlalchemy import SQLAlchemy

from app.utils import GradeEnum

db = SQLAlchemy()


class User(db.Model):
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    city = db.Column(db.String(50))
    info = db.Column(db.String(300))
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)
    meme_grades = db.relationship('MemeGrade', backref='user', passive_deletes=True)

    def __init__(self, name, city, info, email, password):
        self.name = name
        self.city = city
        self.info = info
        self.email = email
        self.password = password

    def __repr__(self):
        return f'User: {self.name} - #{self.id}'


class Meme(db.Model):
    __tablename__ = 'meme'

    id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.String(300), unique=True, nullable=False)
    title = db.Column(db.String(300))
    meme_grades = db.relationship('MemeGrade', backref='meme', passive_deletes=True)

    def __init__(self, url, title):
        self.url = url
        self.title = title

    def __repr__(self):
        return f'Meme #{self.id}: {self.url}'


class MemeGrade(db.Model):
    __tablename__ = 'meme_grade'
    __table_args__ = (
        db.UniqueConstraint('user_id', 'meme_id', name='unique_together_user_meme'),
    )

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id', ondelete="CASCADE"), nullable=False)
    meme_id = db.Column(db.Integer, db.ForeignKey('meme.id', ondelete="CASCADE"), nullable=False)
    grade = db.Column(db.String(10), db.Enum(GradeEnum), nullable=False)

    def __init__(self, user_id, meme_id, grade):
        self.user_id = user_id
        self.meme_id = meme_id
        self.grade = grade

    def __repr__(self):
        return f'Meme #{self.meme_id} - User #{self.user_id} - Grade: {self.grade}'
