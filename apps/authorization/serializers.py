from rest_framework import serializers
from django.contrib.auth.models import User
from .models import UserProfile, ItemCategory, LoanStatus, Loan, MoneyLoan
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=65, min_length=8, write_only=True, style={'input_type': 'password'})
    confirm_password = serializers.CharField(
        max_length=65, min_length=8, write_only=True, style={'input_type': 'password'}
    )
    email = serializers.EmailField(max_length=255, min_length=6)
    first_name = serializers.CharField(max_length=255, min_length=2)
    last_name = serializers.CharField(max_length=255, min_length=2)

    class Meta:
        model = User
        fields = ['pk', 'username', 'email', 'first_name', 'last_name', 'password', 'confirm_password']

    def validate(self, attrs):
        email = attrs.get('email', '')
        password = attrs.get('password', '')
        password_confirm = attrs.pop('confirm_password')
        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError({'email': 'Account with this email exists!'})
        if password != password_confirm:
            raise serializers.ValidationError({'password': 'Passwords must match!'})
        return super().validate(attrs)

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        return token

    def validate(self, attrs):
        data = super().validate(attrs)

        refresh = self.get_token(self.user)

        data['refresh'] = str(refresh)
        data['access'] = str(refresh.access_token)
        data['username'] = self.user.username
        data['email'] = self.user.email
        data['id'] = self.user.id

        return data


class UserProfileSerializer(serializers.HyperlinkedModelSerializer):
    user = UserSerializer()

    class Meta:
        model = UserProfile
        fields = ['url', 'pk', 'user', 'phone_number']

