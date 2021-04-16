import datetime
from django.contrib.auth.models import User
from rest_framework import serializers
from .models import ItemCategory, LoanStatus, Loan, MoneyLoan


class ItemCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemCategory
        fields = ['pk', 'url', 'categoryName']


class LoanStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = LoanStatus
        fields = ['pk', 'url', 'statusName']


class LoanSerializer(serializers.ModelSerializer):
    borrowerID = serializers.SlugRelatedField(queryset=User.objects.all(), slug_field='email')
    itemCategoryID = serializers.SlugRelatedField(queryset=ItemCategory.objects.all(), slug_field='id')

    def _user(self):
        request = self.context.get('request', None)
        if request:
            return request.User

    class Meta:
        model = Loan
        fields = ['pk', 'url', 'name', 'description', 'startDate', 'endDate', 'itemAmount', 'borrowerID',
                  'itemCategoryID', 'image']

    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['itemCategoryID'] = instance.itemCategoryID.categoryName
        response['loanStatusID'] = instance.loanStatusID.statusName
        response['borrowerID'] = instance.borrowerID.username
        response['lenderID'] = instance.lenderID.username

        return response

    def validate(self, attrs):
        start_date = attrs.get('startDate', '')
        end_date = attrs.get('endDate', '')
        if end_date:
            if start_date and end_date < start_date:
                raise serializers.ValidationError({'endDate': 'The end date cannot precede the start date'})
            if end_date < datetime.date.today():
                raise serializers.ValidationError({'endDate': 'The end date cannot be earlier than today'})
        return super().validate(attrs)

    def update(self, instance, validated_data):
        validated_data["startDate"] = instance.startDate
        validated_data["borrowerID"] = instance.borrowerID
        validated_data["itemCategoryID"] = instance.itemCategoryID
        instance = super(LoanSerializer, self).update(instance, validated_data)

        return instance


class MoneyLoanSerializer(serializers.ModelSerializer):
    borrowerID = serializers.SlugRelatedField(queryset=User.objects.all(), slug_field='email')

    def _user(self):
        request = self.context.get('request', None)
        if request:
            return request.User

    class Meta:
        model = MoneyLoan
        fields = ['pk', 'url', 'name', 'description', 'startDate', 'endDate', 'amount', 'borrowerID']

    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['loanStatusID'] = instance.loanStatusID.statusName
        response['borrowerID'] = instance.borrowerID.username
        response['lenderID'] = instance.lenderID.username

        return response

    def validate(self, attrs):
        start_date = attrs.get('startDate', '')
        end_date = attrs.get('endDate', '')
        if end_date:
            if start_date and end_date < start_date:
                raise serializers.ValidationError({'endDate': 'The end date cannot precede the start date'})
            if end_date < datetime.date.today():
                raise serializers.ValidationError({'endDate': 'The end date cannot be earlier than today'})
        return super().validate(attrs)

    def update(self, instance, validated_data):
        validated_data["startDate"] = instance.startDate
        validated_data["borrowerID"] = instance.borrowerID
        validated_data["amount"] = instance.amount
        instance = super(MoneyLoanSerializer, self).update(instance, validated_data)

        return instance
