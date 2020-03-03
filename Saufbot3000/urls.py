"""Saufbot3000 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
import os

from django.conf.urls.static import static
from django.contrib import admin
from django.shortcuts import redirect
from django.urls import path, include

from Saufbot3000 import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path("api/v1/beverage", include("beverage.urls")),
    path("api/v1/beverage/<id>", include("beverage.urls")),
    path("api/v1/pump", include("pump.urls")),
    path("api/v1/recipe", include("recipe.urls")),
    path("api/v1/recipe/<id>", include("recipe.urls")),
    path("api/v1/recipe-beverage", include("recipe_beverage.urls")),
    path("api/v1/recipe-beverage/<id>", include("recipe_beverage.urls")),
]
