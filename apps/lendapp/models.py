from django.contrib.auth.models import User
from django.db import models
from .utils import *
import datetime


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

    def save(self, *args, **kwargs):
        if self._state.adding is True:
            super().save()
            self.create_notification_on_create()
            return
        try:
            _ = Contact.objects.get(user_id=self.lender_id, friend_id=self.borrower_id)
        except Contact.DoesNotExist:
            Contact.objects.create(user_id=self.lender_id, friend_id=self.borrower_id)
        super().save()

    def create_notification(self, date):
        description = "Zbliża się termin zwrotu wypożyczenia \"" + self.name + "\"."
        url = "localhost:3000/loan-items/" + str(self.pk)
        Notification.objects.create(title="Przypomnienie o upływającym terminie", description=description,
                                    is_seen=False, show_date=date, receiver_id=self.borrower_id, frontend_url=url)

    def create_notification_on_update(self):
        description = "Użytkownik " + self.lender_id.username + " dokonał zmian w wypożyczeniu \"" + self.name + "\"."
        url = "localhost:3000/loan-items/" + str(self.pk)
        Notification.objects.create(title="Edycja wypożyczenia", description=description, is_seen=False,
                                    show_date=datetime.date.today(), receiver_id=self.borrower_id, frontend_url=url)

    def create_notification_on_create(self):
        description = "Użytkownik " + self.lender_id.username + " utworzył wypożyczenie \"" + self.name + "\"."
        url = "localhost:3000/loan-items/" + str(self.pk)
        Notification.objects.create(title="Dodanie wypożyczenia", description=description, is_seen=False,
                                    show_date=datetime.date.today(), receiver_id=self.borrower_id, frontend_url=url)

    def create_notification_on_delete(self):
        description = "Użytkownik " + self.lender_id.username + " usunął wypożyczenie \"" + self.name + "\"."
        url = "localhost:3000/loan-items/"
        Notification.objects.create(title="Usunięcie wypożyczenia", description=description, is_seen=False,
                                    show_date=datetime.date.today(), receiver_id=self.borrower_id, frontend_url=url)

    def create_notification_on_return(self):
        description = "Użytkownik " + self.lender_id.username + " przyjął zwrot wypożyczenia \"" + self.name + "\"."
        url = "localhost:3000/loan-items/" + str(self.pk)
        Notification.objects.create(title="Zwrot wypożyczenia", description=description, is_seen=False,
                                    show_date=datetime.date.today(), receiver_id=self.borrower_id, frontend_url=url)

    def create_notification_ask_for_return(self, date):
        description = "Użytkownik " + self.lender_id.username + " prosi o szybszy zwrot wypożyczenia \"" + self.name + \
                      "\". Proponowany termin: " + date
        url = "localhost:3000/loan-items/" + str(self.pk)
        Notification.objects.create(title="Prośba o szybszy zwrot wypożyczenia", description=description, is_seen=False,
                                    show_date=datetime.date.today(), receiver_id=self.borrower_id, frontend_url=url)

    def create_notification_ask_for_longer_return(self, date):
        description = "Użytkownik " + self.lender_id.username + " prosi o wydłużenie terminu zwrotu wypożyczenia \"" + \
                      self.name + "\". Proponowany termin: " + date
        url = "localhost:3000/loan-items/" + str(self.pk)
        Notification.objects.create(title="Prośba o wydłużenie terminu zwrotu wypożyczenia", description=description,
                                    is_seen=False, show_date=datetime.date.today(), receiver_id=self.lender_id,
                                    frontend_url=url)


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

    def save(self, *args, **kwargs):
        if self._state.adding is True:
            super().save()
            self.create_notification_on_create()
            return
        try:
            _ = Contact.objects.get(user_id=self.lender_id, friend_id=self.borrower_id)
        except Contact.DoesNotExist:
            Contact.objects.create(user_id=self.lender_id, friend_id=self.borrower_id)
        super().save()

    def create_notification(self, date):
        description = "Zbliża się termin zwrotu pożyczki \"" + self.name + "\"."
        url = "localhost:3000/loan-money/" + str(self.pk)
        Notification.objects.create(title="Przypomnienie o upływającym terminie", description=description,
                                    is_seen=False, show_date=date, receiver_id=self.borrower_id, frontend_url=url)

    def create_notification_on_update(self):
        description = "Użytkownik " + self.lender_id.username + " dokonał zmian w pożyczce \"" + self.name + "\"."
        url = "localhost:3000/loan-money/" + str(self.pk)
        Notification.objects.create(title="Edycja pożyczki", description=description, is_seen=False,
                                    show_date=datetime.date.today(), receiver_id=self.borrower_id, frontend_url=url)

    def create_notification_on_create(self):
        description = "Użytkownik " + self.lender_id.username + " utworzył pożyczkę \"" + self.name + "\"."
        url = "localhost:3000/loan-money/" + str(self.pk)
        Notification.objects.create(title="Dodanie pożyczki", description=description, is_seen=False,
                                    show_date=datetime.date.today(), receiver_id=self.borrower_id, frontend_url=url)

    def create_notification_on_delete(self):
        description = "Użytkownik " + self.lender_id.username + " usunął pożyczkę \"" + self.name + "\"."
        url = "localhost:3000/loan-money/"
        Notification.objects.create(title="Usunięcie pożyczki", description=description, is_seen=False,
                                    show_date=datetime.date.today(), receiver_id=self.borrower_id, frontend_url=url)

    def create_notification_on_return(self):
        description = "Użytkownik " + self.lender_id.username + " przyjął zwrot pożyczki \"" + self.name + "\"."
        url = "localhost:3000/loan-money/" + str(self.pk)
        Notification.objects.create(title="Zwrot pożyczki", description=description, is_seen=False,
                                    show_date=datetime.date.today(), receiver_id=self.borrower_id, frontend_url=url)

    def create_notification_ask_for_return(self, date):
        description = "Użytkownik " + self.lender_id.username + " prosi o szybszy zwrot pożyczki \"" + self.name + \
                      "\". Proponowany termin: " + date
        url = "localhost:3000/loan-money/" + str(self.pk)
        Notification.objects.create(title="Prośba o szybszy zwrot pożyczki", description=description, is_seen=False,
                                    show_date=datetime.date.today(), receiver_id=self.borrower_id, frontend_url=url)

    def create_notification_ask_for_longer_return(self, date):
        description = "Użytkownik " + self.lender_id.username + " prosi o wydłużenie terminu zwrotu pożyczki \"" + \
                      self.name + "\". Proponowany termin: " + date
        url = "localhost:3000/loan-money/" + str(self.pk)
        Notification.objects.create(title="Prośba o wydłużenie terminu zwrotu pożyczki", description=description,
                                    is_seen=False, show_date=datetime.date.today(), receiver_id=self.lender_id,
                                    frontend_url=url)


class Contact(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, null=False, related_name='contact_list_user_id')
    friend_id = models.ForeignKey(User, on_delete=models.CASCADE, null=False, related_name='contact_list_friend_id')


class Notification(models.Model):
    title = models.CharField(max_length=127, null=False)
    description = models.CharField(max_length=255, null=False)
    is_seen = models.BooleanField(null=False)
    show_date = models.DateField(null=False)
    receiver_id = models.ForeignKey(User, on_delete=models.CASCADE, null=False, related_name='notification_receiver')
    frontend_url = models.URLField(null=True)
