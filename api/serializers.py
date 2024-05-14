from rest_framework import serializers
from django.contrib.auth.models import User
from .models import activity


class UserSerializers(serializers.ModelSerializer):
    class Meta(object):
        model = User
        fields = ['id','username', 'email','password', 'is_active']


class UserPasswordSerializers(serializers.ModelSerializer):
    new_password = serializers.CharField(required=True, write_only=True)

    class Meta(object):
        model = User
        fields = ['email','password', 'new_password']


class UserListSerializers(serializers.ModelSerializer):
    class Meta(object):
        model = User
        fields = ['id', 'username', 'email', 'is_active']    
            

class UserActivitySerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username', read_only=True) 

    class Meta:
        model = activity
        fields = ['id', 'username', 'action', 'timestamp']

class UserSuspensionSerializers(serializers.ModelSerializer):
    class Meta(object):
        model = User
        fields = ['id', 'email', 'is_active']          
