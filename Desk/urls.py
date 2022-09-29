from django import views
from django.urls import path
from . import views
urlpatterns = [
    path('', views.index),
    path('add-a-book',views.add_a_book),
]
