from rest_framework import serializers
from builder.models import Plan

class PlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plan
        fields = ['id', 'title', 'time', 'description', 'location', 'owner']