# Generated by Django 3.1.7 on 2021-04-23 11:12

import apps.lendapp.utils
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ItemCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='LoanStatus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status_name', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='MoneyLoan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=45)),
                ('description', models.CharField(max_length=255, null=True)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField(blank=True, null=True)),
                ('amount', models.FloatField()),
                ('borrower_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='money_loan_borrower', to=settings.AUTH_USER_MODEL)),
                ('lender_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='money_loan_lender', to=settings.AUTH_USER_MODEL)),
                ('loan_status_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='money_loan_loanStatus', to='lendapp.loanstatus')),
            ],
        ),
        migrations.CreateModel(
            name='Loan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=45)),
                ('description', models.CharField(max_length=255, null=True)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField(blank=True, null=True)),
                ('item_amount', models.IntegerField()),
                ('image', models.ImageField(blank=True, null=True, upload_to=apps.lendapp.utils.user_directory_path)),
                ('borrower_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='loan_borrower', to=settings.AUTH_USER_MODEL)),
                ('item_category_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='item_category', to='lendapp.itemcategory')),
                ('lender_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='loan_lender', to=settings.AUTH_USER_MODEL)),
                ('loan_status_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='loan_loan_status', to='lendapp.loanstatus')),
            ],
        ),
    ]