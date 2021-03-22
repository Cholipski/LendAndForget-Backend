from django.urls import path, include
from .views import profile,login_view
from rest_framework import routers
router = routers.DefaultRouter()


urlpatterns = [
    path('profile', profile, name='profile'),
    path('login', login_view, name='login_view'),
    path('api/', include(router.urls))
]