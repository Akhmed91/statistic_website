from django.conf import settings
from django.contrib import admin
from django.urls import include, path
from django.contrib.auth import views

from users.forms import CustomUserChangeForm

urlpatterns = [
    path('', include('statistic_app.urls')),
    path('users/', include('users.urls', namespace='users')),
    path('admin/', admin.site.urls),
]
