from rest_framework import serializers
from builder.models import User, Plan

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'name', 'experience_level', 'is_trainer']

class PlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plan
        fields = ['id', 'title', 'time', 'description', 'place', 'owner']