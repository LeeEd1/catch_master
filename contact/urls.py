from django.urls import path
from . import views

urlpatterns = [
    path('', views.contact, name='contact'),
    path('thankyou/', views.thank_you, name='thank_you'),
]