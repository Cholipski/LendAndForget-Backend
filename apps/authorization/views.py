from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import generics, status
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from .models import UserProfile
from .serializers import UserSerializer, UserProfileSerializer


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
