from flask import abort, make_response

from app.models import Meme, User, meme_schema, user_schema, users_schema
from app.settings import db


def create_user(user):
    """
    This function creates a new user
    based on the passed in user data

    :param user:  user to create in users structure
    :return:  201 on success, 409 on user exists
    """

    email = user.get("email")

    existing_user = User.query.filter(User.email == email).one_or_none()

    if existing_user is None:
        new_user = user_schema.load(user, session=db.session)
        db.session.add(new_user)
        db.session.commit()
        data = user_schema.dump(new_user)

        return data, 201

    else:
        abort(409, f"User with email {email} already exists")


def get_users():
    """
    This function responds to a request for /api/users
    with the complete lists of users

    :return: json string of list of users
    """
    all_users = User.query.order_by(User.city).all()
    data = users_schema.dump(all_users)
    return data


def get_user(user_id):
    """
    This function responds to a request for /api/user/{user_id}
    with one matching user from users

    :param user_id: Id of user to find
    :return:        user matching id or 404
    """
    user = User.query.filter(User.id == user_id).one_or_none()

    if user is not None:
        data = user_schema.dump(user)
        return data
    else:
        abort(404, f"User with Id:{user_id} doesn't exist")


def update_user(user_id, user):
    """
    This function updates an existing user in users structure
    Throws an error if a user with the email we want to update to
    already exists in the database.

    :param user_id:     Id of the user to update in the users structure
    :param user:        user to update
    :return:            updated user structure
    """
    target_user = User.query.filter(User.id == user_id).one_or_none()

    if target_user is None:
        abort(404, f"User wasn't found for Id:{user_id}")

    else:
        update = user_schema.load(user, session=db.session)
        update.id = target_user.id

        db.session.merge(update)
        db.session.commit()

        data = user_schema.dump(target_user)

        return data, 200


def delete_user(user_id):
    """
    This function deletes a user from the users structure

    :param user_id  Id of the user to delete
    :return:        200 on successful delete, 404 if not found
    """

    user = User.query.filter(User.id == user_id).one_or_none()

    if user is not None:
        db.session.delete(user)
        db.session.commit()
        return make_response(f"User Id:{user_id} deleted")

    else:
        abort(404, f"User wasn't found for ID:{user_id}")


def create_meme(meme):

    url = meme.get("url")

    existing_meme = Meme.query.filter(Meme.url == url).one_or_none()

    if existing_meme is None:
        new_meme = meme_schema.load(meme, session=db.session)
        db.session.add(new_meme)
        db.session.commit()
        data = meme_schema.dump(new_meme)

        return data, 201

    else:
        abort(409, f"Meme with url {url} already exists")


def get_meme(meme_id):

    meme = Meme.query.filter(Meme.id == meme_id).one_or_none()

    if meme is not None:
        data = meme_schema.dump(meme)
        return data
    else:
        abort(404, f"Meme with Id:{meme_id} doesn't exist")


def delete_meme(meme_id):

    meme = Meme.query.filter(Meme.id == meme_id).one_or_none()

    if meme is not None:
        db.session.delete(meme)
        db.session.commit()
        return make_response(f"Meme Id:{meme_id} deleted")

    else:
        abort(404, f"Meme wasn't found for ID:{meme_id}")
