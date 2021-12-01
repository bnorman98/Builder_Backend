# Create your views here.

from builder.models import User, Plan
from builder.serializers import UserSerializer, PlanSerializer
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

#Generic views for User class:
class UserList(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = User.objects.all()
    serializer_class = UserSerializer

#Generic views for Plan class:
class PlanList(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Plan.objects.all()
    serializer_class = PlanSerializer

class PlanDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Plan.objects.all()
    serializer_class = PlanSerializer