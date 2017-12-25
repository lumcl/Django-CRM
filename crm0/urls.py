"""crm0 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# from django.contrib import admin
from django.urls import path

from crm import views

urlpatterns = [
    path('', views.index, name="index"),
    path('create-client-form/', views.create_client_form, name="create-client-form"),
    path('edit-client-form/', views.edit_client_form, name="edit-client-form"),
    path('client/', views.client, name="client"),
    path('newClient/', views.newClient, name="newClient"),
    path('editClient/', views.editClient, name="editClient"),
    path('viewClient/', views.viewClient, name="viewClient"),
    path('filter/', views.filter, name="filter"),
    path('notice/', views.notice, name="notice"),
]
