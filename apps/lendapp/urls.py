from django.urls import include, path
from . import views
from django.conf.urls import url
from django.contrib import admin


urlpatterns = [
    path('ItemCategory/', views.ItemCategoryList.as_view(), name=views.ItemCategoryList.name),
    path('ItemCategory/<int:pk>/', views.ItemCategoryDetail.as_view(), name=views.ItemCategoryDetail.name),
    path('LoanStatus/', views.LoanStatusList.as_view(), name=views.LoanStatusList.name),
    path('LoanStatus/<int:pk>/', views.LoanStatusDetail.as_view(), name=views.LoanStatusDetail.name),
    path('Loan/', views.LoanList.as_view(), name=views.LoanList.name),
    path('Loan/<int:pk>/', views.LoanDetail.as_view(), name=views.LoanDetail.name),
    path('return/<int:pk>/', views.ReturnLend.as_view(), name="Return a loan"),
    path('', views.ApiRoot.as_view(), name=views.ApiRoot.name),
]
