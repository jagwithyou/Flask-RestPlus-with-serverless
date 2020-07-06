# SQLAlchemy settings
SQLALCHEMY_DATABASE_URI = 'sqlite:///user_details.db'
# SQLALCHEMY_DATABASE_URI = f'mysql+mysqlconnector://{username}:{password}@{endpoint}/{database_name}'
SQLALCHEMY_TRACK_MODIFICATIONS = True
SECRET_KEY = True

#Defining response codes
rc200 = {200:'success'} 
rc400 = {400:'Bad Request'} 
rc404 = {404:'Not Found'} 
rc500 = {500: 'Internal Server Error'}
rc409 = {409:'Conflict'} 

DEFAULT_RESPONSE_CODES = { **rc200, **rc400, **rc500}