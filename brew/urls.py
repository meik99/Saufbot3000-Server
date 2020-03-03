from django.urls import path

from brew import views

urlpatterns = [
    path("", views.index, name="index")
]