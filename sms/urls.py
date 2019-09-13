from django.urls import path
import django_twilio
from sms import views

app_name = "sms"
urlpatterns = [
     path('api/', views.home, name = 'api'),
     path('send/', views.sms, name = 'send'),
]
