from django.urls import path
from accounts import views
from django.contrib.auth.views import LoginView,LogoutView
app_name = "accounts"

urlpatterns = [
    path('register/',views.register, name="register"),
    path('login/',LoginView.as_view(template_name='accounts/login.html'),name='login'),
    path('logout/',LogoutView.as_view(template_name='accounts/logout.html'),name='logout')
]
