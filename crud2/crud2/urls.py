"""
URL configuration for crud2 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from crud2.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('add-product/', addProduct, name='addProduct'),
    path('edit-product/<str:id>', editProduct, name='editProduct'),
    path('delete-product/<str:id>', deleteProduct, name='deleteProduct'),
    path('view-product/<str:id>', viewProduct, name='viewProduct'),
    path('product-list/', productList, name='productList'),
]
