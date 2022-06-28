from flask import request, jsonify, Blueprint
from app.main import db
from app.models import User
from app.serializers import user_schema, users_schema

routes = Blueprint('routes', __name__)


@routes.route("/user", methods=['POST'])
def add_user():
    name = request.json['name']
    city = request.json['city']
    info = request.json['info']
    email = request.json['info']
    password = request.json['password']

    new_user = User(name, city, info, email, password)

    db.session.add(new_user)
    db.session.commit()

    return user_schema.jsonify(new_user)


@routes.route("/user", methods=['GET'])
def get_users():
    all_users = User.query.all()
    result = users_schema.dump(all_users)
    return jsonify(result)


@routes.route("/user/<pk>", methods=['GET'])
def get_user(pk):
    user = User.query.get(pk)
    return user_schema.jsonify(user)


@routes.route("/user/<pk>", methods=['PUT'])
def update_user(pk):
    user = User.query.get(pk)

    name = request.json['name']
    city = request.json['city']
    info = request.json['info']
    email = request.json['info']
    password = request.json['password']

    user.name = name
    user.city = city
    user.info = info
    user.email = email
    user.password = password

    db.session.commit()

    return user_schema.jsonify(user)


@routes.route("/user/<pk>", methods=['DELETE'])
def delete_user(pk):
    user = User.query.get(pk)
    db.session.delete(user)
    db.session.commit()
    return user_schema.jsonify(user)
