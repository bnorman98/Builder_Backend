# Create your views here.

from django.http.response import JsonResponse
from builder.models import  Plan
from builder.serializers import PlanSerializer
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from django.core.handlers.wsgi import WSGIRequest
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

@api_view(["GET"])
@permission_classes([IsAuthenticated])
def join_session(request : WSGIRequest, pk):
    plan = Plan.objects.get(pk=pk)
    if len(plan.subscribers.filter(pk=request.user.pk)) == 0:
      plan.subscribers.add(request.user)
      plan.save()
    return JsonResponse({"success": "ok"}, safe=False)

# @authentication_classes([SessionAuthentication, BasicAuthentication])
@api_view(["GET"])
@permission_classes([IsAuthenticated])
def get_joinned_sessions(req: WSGIRequest):
  plans = list(Plan.objects.filter(subscribers=req.user))
  plans = list(map(lambda p: p.data, map(PlanSerializer,plans)))
  return JsonResponse(plans, safe=False)