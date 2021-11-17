"""pc_build_admin URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.login, name="login"),
    path('register/', views.register, name="register"),
    path('login_validation/', views.login_validation, name="login_validation"),
    path('manage_admins/', views.manage_admins, name="manage_admins"),
    path('manage_products/', views.manage_products, name="manage_products"),
    path('orders/', views.orders, name="orders"),
    path('logout/', views.logout, name="logout"),
    path('register_admin_firebase/', views.register_admin_firebase, name="register_admin_firebase"),
    path('delete_Admin/', views.delete_Admin, name="delete_Admin"),
    path('edit_Admin/', views.edit_Admin, name="edit_Admin"),
    path('add_product/', views.add_product, name="add_product"),
    
]
