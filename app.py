from flask import Flask , request,jsonify
from flask_sqlalchemy import SQLAlchemy 
from flask_marshmallow import Marshmallow 
from flask_restplus import Api, fields , Resource 
import settings

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']= settings.SQLALCHEMY_DATABASE_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']= settings.SQLALCHEMY_TRACK_MODIFICATIONS 
app.config['SECRET_KEY']= settings.SECRET_KEY
db = SQLAlchemy(app)
ma = Marshmallow(app)
api = Api()
api.init_app(app)

#importing all the endpoints of our app
from API import endpoints

#creating/updating all the database
db.create_all()
   