# Create your views here.

from builder.models import  Plan
from builder.serializers import PlanSerializer
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from django.core.handlers.wsgi import WSGIRequest
import json
from django.http import HttpResponse
from users.models import CustomUser
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

#Generic views for Plan class:
@method_decorator(csrf_exempt, name='dispatch')
class PlanList(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Plan.objects.all()
    serializer_class = PlanSerializer
    
@method_decorator(csrf_exempt, name='dispatch')
class PlanDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Plan.objects.all()
    serializer_class = PlanSerializer
    
def test(request : WSGIRequest, pk):
    
    if request.user is None:
        response_data = {}
        response_data['result'] = 'error'
        response_data['message'] = 'Some error message'
        return HttpResponse(json.dumps(response_data), content_type="application/json")

    plan = Plan.objects.filter(id=pk)[0]
    user = CustomUser.objects.filter(email=request.user.email)[0]

    plan.subscribers.add(user)
    plan.save()

    #user_name = request.user.username
    #print(user_name)
    return HttpResponse(json.dumps({}), content_type="application/json")
