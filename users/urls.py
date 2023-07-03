from django.urls import path

from users.views import *

app_name = 'users'

urlpatterns = [
    path("login/", MyLoginView.as_view(), name="login_page"),
    path("logout/", log_out, name="logout"),
    path('register/',MyRegisterView.as_view(), name='register'),


]