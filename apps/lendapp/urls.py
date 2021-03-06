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
    path('delete-notifications/', views.DeleteNotification.as_view(), name="delete notification"),
    path('delete-all-notifications/', views.DeleteAllNotification.as_view(), name="delete all notification"),
    path('all-notifications-mark-seen/', views.SetAllAsSeen.as_view(), name="Mark all notifications as seen"),
    path('notifications-mark-seen/', views.SetAsSeen.as_view(), name="Mark notification as seen"),
    path('notifications/<int:pk>', views.NotificationDetail.as_view(), name=views.NotificationDetail.name),

    path('request-item-return/', views.RequestEarlierItemReturn.as_view(), name="Request earlier return"),
    path('request-item-longer-time/', views.RequestLongerItemReturnTime.as_view(), name="Request longer return time"),
    path('create-item-reminder/', views.SetItemNotification.as_view(), name="Set reminding notification"),
    path('request-money-return/', views.RequestEarlierMoneyReturn.as_view(), name="Request earlier return"),
    path('request-money-longer-time/', views.RequestLongerMoneyReturnTime.as_view(), name="Request longer return time"),
    path('create-money-reminder/', views.SetMoneyNotification.as_view(), name="Set reminding notification"),

    path('contact/', views.ContactList.as_view(), name=views.ContactList.name),
    path('contact/<int:pk>', views.ContactDetail.as_view(), name=views.ContactDetail.name),

    path('item-return/', views.ReturnLend.as_view(), name="Return a loan"),
    path('money-return/', views.ReturnMoneyLend.as_view(), name="Return money"),


    path('', views.ApiRoot.as_view(), name=views.ApiRoot.name),
]
