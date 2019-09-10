from django.contrib import admin
from django.urls import path
from django.conf.urls import include

urlpatterns = [
    path('chat/', include('chat.urls', namespace='chat')),
    path('admin/', admin.site.urls),
]
