from rest_framework import serializers
from django.contrib.auth.models import User
from .models import activity


class UserSerializers(serializers.ModelSerializer):
    class Meta(object):
        model = User
        fields = ['id','username', 'email','password', 'is_active','is_staff']


class UserListSerializers(serializers.ModelSerializer):
    class Meta(object):
        model = User
        fields = ['id', 'username', 'email', 'is_active','is_staff']    
            

class UserActivitySerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username', read_only=True) 

    class Meta:
        model = activity
        fields = ['id', 'username', 'action', 'timestamp']
        