from django.urls import path

from myemail import views

app_name = "myemail"
urlpatterns = [

     path('send-email/', views.send_email, name = 'send_email'),
]
