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
    lenderID = serializers.ReadOnlyField(source='lenderID.username')
    borrowerID = serializers.HyperlinkedRelatedField(many=True, read_only=True,
                                                     view_name='rest_api: borrower-detail')
    loanStatusID = serializers.SlugRelatedField(queryset=LoanStatus.objects.all(), slug_field='id')
    itemCategoryID = serializers.SlugRelatedField(queryset=ItemCategory.objects.all(), slug_field='id')

    class Meta:
        model = Loan
        fields = ['pk', 'url', 'name',
                  'description', 'startDate', 'endDate',
                  'itemAmount', 'lenderID', 'borrowerID',
                  'loanStatusID', 'itemCategoryID']
