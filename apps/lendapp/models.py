from django.contrib.auth.models import User
from django.db import models
from .utils import *


class ItemCategory(models.Model):
    category_name = models.CharField(max_length=20, null=False)

    def __str__(self):
        return self.category_name


class LoanStatus(models.Model):
    status_name = models.CharField(max_length=15, null=False)

    def __str__(self):
        return self.status_name


class Loan(models.Model):
    name = models.CharField(max_length=45, null=False)
    description = models.CharField(max_length=255, null=True)
    start_date = models.DateField(null=False)
    end_date = models.DateField(null=True, blank=True)
    item_amount = models.IntegerField(null=False)
    lender_id = models.ForeignKey(User, on_delete=models.CASCADE, null=False, related_name='loan_lender')
    borrower_id = models.ForeignKey(User, on_delete=models.CASCADE, null=False, related_name='loan_borrower')
    loan_status_id = models.ForeignKey(LoanStatus, on_delete=models.CASCADE, null=False,
                                       related_name='loan_loan_status')
    item_category_id = models.ForeignKey(ItemCategory, on_delete=models.CASCADE, null=False,
                                         related_name='item_category')
    image = models.ImageField(upload_to=user_directory_path, null=True, blank=True)


class MoneyLoan(models.Model):
    name = models.CharField(max_length=45, null=False)
    description = models.CharField(max_length=255, null=True)
    start_date = models.DateField(null=False)
    end_date = models.DateField(null=True, blank=True)
    amount = models.FloatField(null=False)
    loan_status_id = models.ForeignKey(LoanStatus, on_delete=models.CASCADE, null=False, related_name='money_loan'
                                                                                                      '_loanStatus')
    lender_id = models.ForeignKey(User, on_delete=models.CASCADE, null=False, related_name='money_loan_lender')
    borrower_id = models.ForeignKey(User, on_delete=models.CASCADE, null=False, related_name='money_loan_borrower')


class Notification(models.Model):
    title = models.CharField(max_length=45, null=False)
    description = models.CharField(max_length=255, null=False)
    is_seen = models.BooleanField(null=False)
    show_date = models.DateField(null=False)
    receiver_id = models.ForeignKey(User, on_delete=models.CASCADE, null=False, related_name='notification_receiver')
