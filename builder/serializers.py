from allauth.account.utils import default_user_display
from rest_framework import serializers
from builder.models import Plan
from users.serializers import UserSerializer
from rest_framework.fields import CurrentUserDefault

class PlanSerializer(serializers.ModelSerializer):
    owner = UserSerializer(required=False)

    def save(self):
      owner = self.context['request'].user
      plan = super().save(owner=owner)
      return plan
    class Meta:
        model = Plan
        fields = ['id', 'title', 'time', 'description', 'location', 'owner', 'experience_level']