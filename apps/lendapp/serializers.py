import datetime
from django.contrib.auth.models import User
from rest_framework import serializers
from .models import ItemCategory, LoanStatus, Loan, MoneyLoan, Notification, Contact


class ItemCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemCategory
        fields = ['pk', 'url', 'category_name']


class LoanStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = LoanStatus
        fields = ['pk', 'url', 'status_name']


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ['pk', 'user_id', 'friend_id']

    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['friend_first_name'] = instance.friend_id.first_name
        response['firend_last_name'] = instance.friend_id.last_name
        response['firend_email'] = instance.friend_id.email

        return response


class LoanSerializer(serializers.ModelSerializer):
    borrower_id = serializers.SlugRelatedField(queryset=User.objects.all(), slug_field='email')
    item_category_id = serializers.SlugRelatedField(queryset=ItemCategory.objects.all(), slug_field='id')

    def _user(self):
        request = self.context.get('request', None)
        if request:
            return request.User

    class Meta:
        model = Loan
        fields = ['pk', 'url', 'name', 'description', 'start_date', 'end_date', 'item_amount', 'borrower_id',
                  'item_category_id', 'image']

    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['item_category_id'] = instance.item_category_id.category_name
        response['loan_status_id'] = instance.loan_status_id.status_name
        response['borrower_id'] = instance.borrower_id.username
        response['lender_id'] = instance.lender_id.username

        return response

    def validate(self, attrs):
        start_date = attrs.get('start_date', '')
        end_date = attrs.get('end_date', '')
        if end_date:
            if start_date and end_date < start_date:
                raise serializers.ValidationError({'end_date': 'The end date cannot precede the start date'})
            if end_date < datetime.date.today():
                raise serializers.ValidationError({'end_date': 'The end date cannot be earlier than today'})
        return super().validate(attrs)

    def update(self, instance, validated_data):
        validated_data["start_date"] = instance.start_date
        validated_data["borrower_id"] = instance.borrower_id
        validated_data["item_category_id"] = instance.item_category_id
        instance = super(LoanSerializer, self).update(instance, validated_data)

        return instance


class MoneyLoanSerializer(serializers.ModelSerializer):
    borrower_id = serializers.SlugRelatedField(queryset=User.objects.all(), slug_field='email')

    def _user(self):
        request = self.context.get('request', None)
        if request:
            return request.User

    class Meta:
        model = MoneyLoan
        fields = ['pk', 'url', 'name', 'description', 'start_date', 'end_date', 'amount', 'borrower_id']

    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['loan_status_id'] = instance.loan_status_id.status_name
        response['borrower_id'] = instance.borrower_id.username
        response['lender_id'] = instance.lender_id.username

        return response

    def validate(self, attrs):
        start_date = attrs.get('start_date', '')
        end_date = attrs.get('end_date', '')
        if end_date:
            if start_date and end_date < start_date:
                raise serializers.ValidationError({'end_date': 'The end date cannot precede the start date'})
            if end_date < datetime.date.today():
                raise serializers.ValidationError({'end_date': 'The end date cannot be earlier than today'})
        return super().validate(attrs)

    def update(self, instance, validated_data):
        validated_data["start_date"] = instance.start_date
        validated_data["borrower_id"] = instance.borrower_id
        validated_data["amount"] = instance.amount
        instance = super(MoneyLoanSerializer, self).update(instance, validated_data)

        return instance


class NotificationSerializer(serializers.ModelSerializer):
    receiver_id = serializers.SlugRelatedField(queryset=User.objects.all(), slug_field='id')

    def _user(self):
        request = self.context.get('request', None)
        if request:
            return request.User

    class Meta:
        model = Notification
        fields = ['pk', 'url', 'title', 'description', 'is_seen', 'show_date', 'receiver_id']

