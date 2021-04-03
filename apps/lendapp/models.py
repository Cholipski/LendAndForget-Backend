from django.contrib.auth.models import User
from django.db import models



class ItemCategory(models.Model):
    categoryName = models.CharField(max_length=20, null=False)

    def __str__(self):
        return self.categoryName


class LoanStatus(models.Model):
    statusName = models.CharField(max_length=15, null=False)

    def __str__(self):
        return self.statusName


class Loan(models.Model):
    name = models.CharField(max_length=45, null=False)
    description = models.CharField(max_length=255, null=True)
    startDate = models.DateField(null=False)
    endDate = models.DateField(null=True)
    itemAmount = models.IntegerField(null=False)
    lenderID = models.ForeignKey(User, on_delete=models.CASCADE, null=False, related_name='Loan_lender')
    borrowerID = models.ForeignKey(User, on_delete=models.CASCADE, null=False, related_name='Loan_borrower')
    loanStatusID = models.ForeignKey(LoanStatus, on_delete=models.CASCADE, null=False, related_name='Loan_loanStatus')
    itemCategoryID = models.ForeignKey(ItemCategory, on_delete=models.CASCADE, null=False, related_name='ItemCategory')

class MoneyLoan(models.Model):
    name = models.CharField(max_length=45, null=False)
    description = models.CharField(max_length=255, null=True)
    startDate = models.DateField(null=False)
    endDate = models.DateField(null=True)
    amount = models.FloatField(null=False)
    loanStatusID = models.ForeignKey(LoanStatus, on_delete=models.CASCADE, null=False, related_name='MoneyLoan'
                                                                                                    '_loanStatus')
    lenderID = models.ForeignKey(User, on_delete=models.CASCADE, null=False, related_name='MoneyLoan_lender')
    borrowerID = models.ForeignKey(User, on_delete=models.CASCADE, null=False, related_name='MoneyLoan_borrower')
