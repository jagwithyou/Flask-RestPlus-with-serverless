from app import ma

class UserSchema(ma.Schema):
    class Meta:
        fields = ('id','name','email','password')