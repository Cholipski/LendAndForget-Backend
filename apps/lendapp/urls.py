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
    path('item-return/', views.ReturnLend.as_view(), name="Return a loan"),
    path('', views.ApiRoot.as_view(), name=views.ApiRoot.name),
]
