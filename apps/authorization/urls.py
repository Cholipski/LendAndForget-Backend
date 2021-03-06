from django.urls import path, include
from rest_framework_simplejwt.views import (
	TokenRefreshView,
)
from . import views
from rest_framework import routers

router = routers.DefaultRouter()

urlpatterns = [
	path('', views.MyTokenObtainPairView.as_view(), name='Login'),
	path('token-refresh/', TokenRefreshView.as_view(), name='Token refresh'),
	path('register/', views.RegisterView.as_view(), name=views.RegisterView.name),
	path('email-verify/', views.VerifyEmail.as_view(), name="email-verify"),
	path('user-manage/', views.UserManage.as_view(), name="user-manage"),
	path('usersprofile/', views.UserProfileList.as_view(), name=views.UserProfileList.name),
	path('usersprofile/<int:pk>', views.UserProfileDetail.as_view(), name=views.UserProfileDetail.name),
	path('api/', include(router.urls))
]
