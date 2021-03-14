from django.urls import path, include
from .views import  RegisterAPI, ContentViewSet 
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token

router = DefaultRouter()
router.register('content', ContentViewSet, basename='content')


urlpatterns = [
    path('', include(router.urls)),
    path('register/', RegisterAPI.as_view(), name='register'),
    path('login/', obtain_auth_token, name='login'),  
]