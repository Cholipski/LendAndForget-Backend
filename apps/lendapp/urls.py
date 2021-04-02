from django.urls import include, path
from . import views
from django.conf.urls import url
from django.contrib import admin


urlpatterns = [
    path('ItemCategory/', views.ItemCategoryList.as_view(), name=views.ItemCategoryList.name),
    path('ItemCategory/<int:pk>/', views.ItemCategoryDetail.as_view(), name=views.ItemCategoryDetail.name),
    path('', views.ApiRoot.as_view(), name=views.ApiRoot.name),
]
