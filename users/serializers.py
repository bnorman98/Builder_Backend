from rest_framework import serializers
from rest_auth.registration.serializers import RegisterSerializer
from rest_framework.request import Request

from users.models import CustomUser


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = CustomUser
        fields = ['id', 'email', 'username', 'exp_level', 'name', 'first_name']


class RegisterSerializer(RegisterSerializer):

    def save(self, request: Request):
      user = super().save(request)
      user.first_name = request.data['first_name']
      user.save()
      return user
      
