from django.urls import path
from builder import views
from rest_framework.urlpatterns import format_suffix_patterns
from allauth.account.views import confirm_email
from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('user/', views.UserList.as_view()),
    path('user/<int:pk>/', views.UserDetail.as_view()),
    path('plan/', views.PlanList.as_view()),
    path('plan/<int:pk>/', views.PlanDetail.as_view()),
    
    path('admin/', admin.site.urls),
    url(r'^rest-auth/', include('rest_auth.urls')),
    url(r'^rest-auth/registration/', include('rest_auth.registration.urls')),
    url(r'^account/', include('allauth.urls')),
    url(r'^accounts-rest/registration/account-confirm-email/(?P<key>.+)/$', confirm_email, name='account_confirm_email'),                                                                                       
]
urlpatterns = format_suffix_patterns(urlpatterns)