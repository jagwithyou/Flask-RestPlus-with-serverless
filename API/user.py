from flask import  jsonify, make_response
from database.db_schema import UserSchema
from database.model import User
from app import db

#Initializing Marshmallow Schema
user_schema = UserSchema()
users_schema = UserSchema(many=True)

def get_users(data):
    try:
        return jsonify(users_schema.dump(User.query.all()))
    except Exception as e:
        return make_response(jsonify({'message': e.__doc__}), 500)

def create_user(data):
    try:
        user = User(name=data['name'],email=data['email'],password=data['password'])
        db.session.add(user)
        db.session.commit()
        return make_response(jsonify({'message':'data added to database', 'user_id': user.id}), 200)
    except Exception as e:
        return make_response(jsonify({'message': e.__doc__}), 500)

def update_user(data,id):
    try:
        user = User.query.get(id)
        if user:
            user.name, user.email, user.password = data['name'], data['email'], data['password']
            db.session.commit()
            return make_response(jsonify({'message':'data updated to database'}), 200)
        return make_response(jsonify({'message':'User Not Found'}), 404)
    except Exception as e:
        return make_response(jsonify({'message': e.__doc__}), 500)

def delete_user(data,id):
    try:
        user = User.query.get(id)
        if user:
            db.session.delete(user)
            db.session.commit()
            return make_response(jsonify({'message':'data deleted successfully'}), 200)
        return make_response(jsonify({'message':'User Not Found'}), 404)
    except Exception as e:
        return make_response(jsonify({'message': e.__doc__}), 500)