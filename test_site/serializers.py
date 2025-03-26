import logging
from rest_framework import serializers
from test_site.models import User, Role

logger = logging.getLogger('main')


class UserCreateSerializer(serializers.ModelSerializer):

    class Meta():
        model = User
        fields = ('email', 'password')


class UserSerializer(serializers.ModelSerializer):

    class Meta():
        model = User
        fields = ('email', 'password', 'about', 'avatar')


class RoleSerializer(serializers.ModelSerializer):

    class Meta:
        model = Role
        field = '__all__'
