from flask import Flask, jsonify,request, make_response
from flask_restplus import  Resource
from app import api
from API.serializers.user_serializer import model
from API import user
from settings import DEFAULT_RESPONSE_CODES, rc409

ns_users = api.namespace('user', title="User Module", description=('APIs For User Management'))

@ns_users.route('')
class UserDetails(Resource):
    @ns_users.doc(responses=DEFAULT_RESPONSE_CODES, description="Get list of all the Users")
    def get(self):
        return user.get_users(request.json)

    @ns_users.doc(responses={**DEFAULT_RESPONSE_CODES, **rc409}, description="Create a new user")
    @api.expect(model)
    def post(self):
        return user.create_user(request.json)

@ns_users.route('/<int:id>')
@ns_users.doc(responses=DEFAULT_RESPONSE_CODES, params={'id': 'Specify the Id associated with the User'})
class UpdateDelete(Resource):
    @ns_users.doc(description="Update the specific User")
    @api.expect(model)
    def put(self,id):
        return user.update_user(request.json, id)
    @ns_users.doc(description="Delete the specific User")
    def delete(self,id):
        return user.delete_user(request.json, id)