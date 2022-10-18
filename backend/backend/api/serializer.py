# from typing_extensions import Required
# from xml.sax.xmlreader import AttributesImpl
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework import serializers
from rest_framework.validators import UniqueValidator

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls,user):
        token=super().get_token(user)
        token['username']=user.username
        token['email']=user.email
        return token
class RegisterSerializer(serializers.ModelSerializer):
    password=serializers.CharField(write_only=True,required=True,validators=[validate_password])
    password2=serializers.CharField(write_only=True,required=True)
    loginkey=serializers.CharField(write_only=True,required=True)

    class Meta:
        model=User
        fields=('username','password','password2','loginkey')
    
    def validate(self,attrs):
        if(attrs['password']!=attrs['password2']):
            raise serializers.ValidationError({"password":"password dosen't match"})
        # if(attrs['key']!='staffkey'):
        #     raise serializers.ValidationError({"staffkey":"staffkey dosent match"})
        return attrs

    def create(self,validated_data):
        user=User.objects.create(username=validated_data['username'],loginkey=validated_data['loginkey'])
        user.set_password(validated_data['password'])
        user.save()

        return user
        