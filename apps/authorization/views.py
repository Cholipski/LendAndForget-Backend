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
from .serializers import UserSerializer, UserProfileSerializer, MyTokenObtainPairSerializer, PasswordSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from .utils import Util
from django.conf import settings


@permission_classes([AllowAny])
class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


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
            url = 'http:/localhost/email-verify/' + str(token)
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


class UserManage(generics.GenericAPIView):
    def get(self, request):
        user = request.user
        serializer = UserSerializer(user, many=False)

        userprofile = UserProfile.objects.get(user_id=serializer.data['pk'])
        serializer2 = UserProfileSerializer(userprofile, many=False)
        response = serializer.data
        response['phone'] = serializer2.data['phone_number']
        return Response(response)

    def delete(self, request):
        res = {
            'status': '',
            'message': '',
        }
        user = User.objects.get(username=self.request.user)
        user.delete()
        res['status'] = 'success'
        res['message'] = 'Successfully account deleted'

        return JsonResponse(res)

    def put(self, request):
        try:
            user = request.user
            serializer = UserSerializer(user, many=False)
            userprofile = UserProfile.objects.get(user_id=serializer.data['pk'])
            data = request.data

            if data['first_name'] != '':
                user.first_name = data['first_name']

            if data['last_name'] != '':
                user.last_name = data['last_name']

            if data['phone'] != '':
                userprofile.phone_number = data['phone']

            if data['old_password'] != '' or data['new_password'] != '' or data['re_password'] != '':
                serializer_pass = PasswordSerializer(data=request.data)
                if serializer_pass.is_valid():
                    if not user.check_password(serializer_pass.data.get('old_password')):
                        return Response({'status': ['Wrong old password.']},
                                        status=status.HTTP_400_BAD_REQUEST)
                    if data['new_password'] != data['re_password']:
                        return Response({'status': ['Passwords must match!.']},
                                        status=status.HTTP_400_BAD_REQUEST)
                    user.set_password(data['new_password'])

            if (data['first_name'] == '' and data['last_name'] == ''
                    and data['phone'] == '' and data['old_password'] ==''
                    and data['new_password'] == '' and data['re_password'] == ''):
                return Response({'status': ['Nothing was changed']},
                                status=status.HTTP_200_OK)
            user.save()
            userprofile.save()
            return Response({'status': 'Data changed successfully'}, status=status.HTTP_200_OK)
        except Exception:
            return Response({'status': 'Something went wrong'}, status=status.HTTP_400_BAD_REQUEST)

class ApiRoot(generics.GenericAPIView):
    name = 'api-root'

    def get(self, request, *args, **kwargs):
        return Response({'usersprofile': reverse(UserProfileList.name),
                         'register': reverse(RegisterView.name),
                         })
