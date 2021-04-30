from django.urls import include, path
from . import views
from django.conf.urls import url
from django.contrib import admin


urlpatterns = [
    path('category/', views.ItemCategoryList.as_view(), name=views.ItemCategoryList.name),
    path('category/<int:pk>', views.ItemCategoryDetail.as_view(), name=views.ItemCategoryDetail.name),

    path('loan-status/', views.LoanStatusList.as_view(), name=views.LoanStatusList.name),
    path('loan-status/<int:pk>', views.LoanStatusDetail.as_view(), name=views.LoanStatusDetail.name),

    path('item-loan/', views.LoanList.as_view(), name=views.LoanList.name),
    path('item-loan/<int:pk>', views.LoanDetail.as_view(), name=views.LoanDetail.name),

    path('money-loan/', views.MoneyLoanList.as_view(), name=views.MoneyLoanList.name),
    path('money-loan/<int:pk>', views.MoneyLoanDetail.as_view(), name=views.MoneyLoanDetail.name),

    path('notifications/', views.NotificationList.as_view(), name=views.NotificationList.name),
    path('notifications/<int:pk>', views.NotificationDetail.as_view(), name=views.NotificationDetail.name),

    path('contact/', views.ContactList.as_view(), name=views.ContactList.name),
    path('contact/<int:pk>', views.ContactDetail.as_view(), name=views.ContactDetail.name),

    path('item-return/', views.ReturnLend.as_view(), name="Return a loan"),
    path('money-return/', views.ReturnMoneyLend.as_view(), name="Return money"),
    path('notifications-mark-seen/', views.SetAsSeen.as_view(), name="Return money"),

    path('', views.ApiRoot.as_view(), name=views.ApiRoot.name),
]
