from django.urls import path
from . import views

urlpatterns = [
    path('', views.catch_cam, name='catch_cam'),
    path('add/', views.add_catch, name='add_catch'),
    path('edit/<int:catch_id>/', views.edit_catch, name='edit_catch'),
    path('delete/<int:catch_id>/', views.delete_catch, name='delete_catch'),
]
