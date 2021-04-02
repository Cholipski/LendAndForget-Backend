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
    lenderID = serializers.SerializerMethodField('_user')
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
                  'itemAmount', 'lenderID', 'borrowerID',
                  'loanStatusID', 'itemCategoryID']
