import json

import jwt
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.urls import reverse
from rest_framework import generics, status
from rest_framework.decorators import permission_classes
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from .models import UserProfile
from .serializers import UserSerializer, UserProfileSerializer, MyTokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from .utils import Util
from django.conf import settings


@permission_classes([AllowAny])
class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


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


@permission_classes([AllowAny])
class RegisterView(GenericAPIView):
    serializer_class = UserSerializer
    name = 'register'

    def post(self, request):
        serializer = UserSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            user = User.objects.get(email=serializer.data['email'])
            user.is_active = False
            user.save()
            token = RefreshToken.for_user(user)
            relative_link = reverse('email-verify')

            url = 'http://localhost:3000' + relative_link + "/" + str(token)
            email_body = "Hi " + user.username + '! \nUse link below to activate your account!. \n' + url
            data = {"to_email": user.email, "email_body": email_body, 'email_subject': 'Verify your email!'}
            Util.send_activation_email(data)
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class VerifyEmail(generics.GenericAPIView):
    def post(self, request):
        token = json.loads(request.body)
        res = {
            'status': '',
            'message': '',
        }
        try:
            payload = jwt.decode(token, settings.SECRET_KEY, algorithms=["HS256"])
            user = User.objects.get(id=payload['user_id'])
            if not user.is_active:
                user.is_active = True
                user.save()
                res['status'] = 'success'
                res['message'] = 'Successfully activated'

            return JsonResponse(res)

        except jwt.ExpiredSignatureError:
            res['status'] = 'failed'
            res['message'] = 'Activation expired'
            return JsonResponse(res)

        except jwt.exceptions.DecodeError:
            res['status'] = 'failed'
            res['message'] = 'Invalid token'
            return JsonResponse(res)


class ApiRoot(generics.GenericAPIView):
    name = 'api-root'

    def get(self, request, *args, **kwargs):
        return Response({'users': reverse(UserList.name),
                         'usersprofile': reverse(UserProfileList.name),
                         'register': reverse(RegisterView.name),
                         })
