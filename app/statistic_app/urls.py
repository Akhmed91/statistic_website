from django.conf import settings
from django.contrib import admin
from django.urls import include, path
from .views import IndexListView

app_name = 'statistic_app'

urlpatterns = [
    path('', IndexListView.as_view(), name='index'),
]
