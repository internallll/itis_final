from django.contrib.auth import authenticate
from rest_framework import serializers
from yaml import serialize

from test_site.models import User
from django.utils.translation import gettext_lazy as _


class RegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        max_length=128,
        min_length=8,
        write_only=True,
    )


    class Meta:
        model = User
        fields = ('email', 'password','first_name','last_name','birth_date','role')

    def create(self, validated_data):
        user = User(**validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user
# class LoginSerializer(serializers.Serializer):
#
#     email = serializers.EmailField(write_only=True)
#     password = serializers.CharField(max_length=128, write_only=True)
#
#     username = serializers.CharField(max_length=255, read_only=True)
#     token = serializers.CharField(max_length=255, read_only=True)
#
#     def validate(self, data):
#         """
#         Validates user data.
#         """
#         email = data.get('email', None)
#         password = data.get('password', None)
#
#
#
#         if email is None:
#             raise serializers.ValidationError(
#                 'An email address is required to log in.'
#             )
#
#         if password is None:
#             raise serializers.ValidationError(
#                 'A password is required to log in.'
#             )
#
#         user = authenticate(username=email, password=password)
#
#         if user is None:
#             raise serializers.ValidationError(
#                 'A user with this email and password was not found.'
#             )
#
#         if not user.is_active:
#             raise serializers.ValidationError(
#                 'This user has been deactivated.'
#             )
#
#         return {
#             'token': user.token,
#         }

class AuthTokenSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)

    def validate(self, attrs):
        email = attrs.get('email')
        password = attrs.get('password')

        if email and password:
            user = authenticate(request=self.context.get('request'),
                                username=email, password=password)
            if not user:
                message = _('Unable to log in with provided credentials.')
                raise serializers.ValidationError(message, code='authorization')
        else:
            message = _('Must include "email" and "password".')
            raise serializers.ValidationError(message, code='authorization')

        attrs['user'] = user
        return attrs