from django.urls import path, include
from rest_framework_simplejwt.views import (
	TokenRefreshView,
)
from . import views
from rest_framework import routers

router = routers.DefaultRouter()

urlpatterns = [
	path('users', views.UserList.as_view(), name=views.UserList.name),
	path('users/<int:pk>', views.UserDetail.as_view(), name=views.UserDetail.name),
	path('usersprofile', views.UserProfileList.as_view(), name=views.UserProfileList.name),
	path('usersprofile/<int:pk>', views.UserProfileDetail.as_view(), name=views.UserProfileDetail.name),
	path('register', views.RegisterView.as_view(), name=views.RegisterView.name),
	path('email-verify', views.VerifyEmail.as_view(), name="email-verify"),
	path('', views.ApiRoot.as_view(), name=views.ApiRoot.name),
	path('user/login/', views.MyTokenObtainPairView.as_view(), name='Login'),
	path('user/login-refresh/', TokenRefreshView.as_view(), name='Token refresh'),
	path('api/', include(router.urls))
]