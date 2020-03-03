from django.urls import path

from recipe_beverage import views

urlpatterns = [
    path("", views.index, name="index")
]