from django.urls import path
from rest_framework_simplejwt import views as jwt_views
from . import views

urlpatterns = [
	path('users', views.UserList.as_view(), name=views.UserList.name),
	path('users/<int:pk>', views.UserDetail.as_view(), name=views.UserDetail.name),
	path('usersprofile', views.UserProfileList.as_view(), name=views.UserProfileList.name),
	path('usersprofile/<int:pk>', views.UserProfileDetail.as_view(), name=views.UserProfileDetail.name),
	path('register', views.RegisterView.as_view(), name=views.RegisterView.name),
	path('', views.ApiRoot.as_view(), name=views.ApiRoot.name),
	path('api/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
	path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
]
