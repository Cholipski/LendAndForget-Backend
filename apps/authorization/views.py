from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import generics, status, exceptions
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from .models import UserProfile
from .serializers import UserSerializer, UserProfileSerializer
from django.contrib.auth import get_user_model
from rest_framework.permissions import AllowAny
from rest_framework.decorators import api_view, permission_classes
from django.views.decorators.csrf import ensure_csrf_cookie
from .utils import generate_access_token, generate_refresh_token

class UserList(generics.ListAPIView):
	queryset = User.objects.all()
	serializer_class = UserSerializer
	name = 'user-list'


class UserDetail(generics.RetrieveAPIView):
	queryset = User.objects.all()
	serializer_class = UserSerializer
	name = 'user-detail'


class UserProfileList(generics.ListAPIView):
	queryset = UserProfile.objects.all()
	serializer_class = UserProfileSerializer
	name = 'userprofile-list'


class UserProfileDetail(generics.RetrieveAPIView):
	queryset = UserProfile.objects.all()
	serializer_class = UserProfileSerializer
	name = 'userprofile-detail'


class ApiRoot(generics.GenericAPIView):
	name = 'api-root'

	def get(self, request, *args, **kwargs):
		return Response({'users': reverse(UserList.name),
						 'usersprofile': reverse(UserProfileList.name),
						 'register': reverse(RegisterView.name)
						 })


class RegisterView(GenericAPIView):
	serializer_class = UserSerializer
	name = 'register'

	def post(self, request):
		serializer = UserSerializer(data=request.data)

		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_200_OK)

		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
@permission_classes([AllowAny])
@ensure_csrf_cookie
def login_view(request):
    User = get_user_model()
    username = request.data.get('username')
    password = request.data.get('password')
    response = Response()
    if (username is None) or (password is None):
        raise exceptions.AuthenticationFailed(
            'username and password required')

    user = User.objects.filter(username=username).first()
    if(user is None):
        raise exceptions.AuthenticationFailed('user not found')
    if (not user.check_password(password)):
        raise exceptions.AuthenticationFailed('wrong password')

    serialized_user = UserSerializer(user).data

    access_token = generate_access_token(user)
    refresh_token = generate_refresh_token(user)

    response.set_cookie(key='refreshtoken', value=refresh_token, httponly=True)
    response.data = {
        'access_token': access_token,
        'user': serialized_user,
    }

    return response

@api_view(['GET'])
def profile(request):
    user = request.user
    serialized_user = UserSerializer(user).data
    return Response({'user': serialized_user })
