from flask_restplus import fields
from app import  api

model = api.model('demo',{
    'name':fields.String('Enter Name'),
    'email':fields.String('Enter Email'),
    'password':fields.String('Enter Password')
})