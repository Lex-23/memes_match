from functools import wraps

import jwt
from flask import current_app, jsonify, request

from app.models import User


def token_required(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        token = None
        if "x-access-token" in request.headers:
            token = request.headers["x-access-token"]
        if not token:
            return jsonify({"message": "Token is missing !!"}), 401
        try:
            data = jwt.decode(
                token, current_app.config["SECRET_KEY"], algorithms=["HS256"]
            )
            current_user = User.query.filter_by(id=data["id"])
        except Exception as e:
            return jsonify({"message": e})
        breakpoint()
        return func(current_user, *args, **kwargs)

    return wrapper
