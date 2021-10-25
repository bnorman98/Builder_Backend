from django.urls import path
from builder import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('user/', views.UserList.as_view()),
    path('user/<int:pk>/', views.UserDetail.as_view()),
    path('plan/', views.PlanList.as_view()),
    path('plan/<int:pk>/', views.PlanDetail.as_view()),
]
urlpatterns = format_suffix_patterns(urlpatterns)
