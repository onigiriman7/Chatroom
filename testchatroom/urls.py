from django.contrib import admin
from django.urls import path
from django.conf.urls import include

urlpatterns = [
    path('chat/', include('chat.urls', namespace='chat')),
    path('accounts/',include('accounts.urls',namespace = 'accounts')),
    path('sms/',include('sms.urls', namespace = 'sms')),
    path('email/',include('myemail.urls', namespace = 'email')),
    path('admin/', admin.site.urls),
]
