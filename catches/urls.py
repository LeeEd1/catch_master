from django.urls import path
from . import views

urlpatterns = [
    path('', views.catch_cam, name='catch_cam'),
    path('add/', views.add_catch, name='add_catch'),
]