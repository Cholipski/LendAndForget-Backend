from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


class UserProfile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	phone_number = models.TextField(max_length=25, null=True)

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
	lenderID = models.ForeignKey(User, on_delete=models.CASCADE, null=False, related_name='Lender')
	borrowerID = models.ForeignKey(User, on_delete=models.CASCADE, null=False, related_name='Borrower')
	loanStatusID = models.ForeignKey(LoanStatus, on_delete=models.CASCADE, null=False, related_name='LoanStatus')
	itemCategoryID = models.ForeignKey(ItemCategory, on_delete=models.CASCADE, null=False, related_name='ItemCategory')

class MoneyLoan(models.Model):
	name = models.CharField(max_length=45, null=False)
	description = models.CharField(max_length=255, null=True)
	startDate = models.DateField(null=False)
	endDate = models.DateField(null=True)
	amount = models.FloatField(null=False)
	loanStatusID = models.ForeignKey(LoanStatus, on_delete=models.CASCADE, null=False, related_name='LoanStatus')
	lenderID = models.ForeignKey(User, on_delete=models.CASCADE, null=False, related_name='Lender')
	borrowerID = models.ForeignKey(User, on_delete=models.CASCADE, null=False, related_name='Borrower')


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
	if created:
		UserProfile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
	instance.userprofile.save()
