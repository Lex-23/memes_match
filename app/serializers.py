from flask_marshmallow import Marshmallow

ma = Marshmallow()


class UserSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name', 'city', 'info', 'email', 'password')


user_schema = UserSchema()
users_schema = UserSchema(many=True)
