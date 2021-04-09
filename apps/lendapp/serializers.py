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
    borrowerID = serializers.SlugRelatedField(queryset=User.objects.all(), slug_field='id')
    loanStatusID = serializers.SlugRelatedField(queryset=LoanStatus.objects.all(), slug_field='id')
    itemCategoryID = serializers.SlugRelatedField(queryset=ItemCategory.objects.all(), slug_field='id')

    def _user(self, obj):
        request = self.context.get('request', None)
        if request:
            return request.User

    class Meta:
        model = Loan
        fields = ['pk', 'url', 'name',
                  'description', 'startDate', 'endDate',
                  'itemAmount', 'borrowerID',
                  'loanStatusID', 'itemCategoryID']

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep['itemCategoryID'] = instance.itemCategoryID.categoryName
        rep['loanStatusID'] = instance.loanStatusID.statusName
        rep['borrowerID'] = instance.borrowerID.username
        rep['lenderID'] = instance.lenderID.username

        return rep

    def validate(self, attrs):
        startDate = attrs.get('startDate', '')
        endDate = attrs.get('endDate', '')
        if endDate:
            if startDate and endDate < startDate:
                raise serializers.ValidationError({'endDate': 'The end date cannot precede the start date'})
            if endDate < datetime.date.today():
                raise serializers.ValidationError({'endDate': 'The end date cannot be earlier than today'})
        return super().validate(attrs)

