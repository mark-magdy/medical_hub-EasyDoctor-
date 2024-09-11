from django.urls import path, include
from django.conf import settings
from . import views
from django.contrib.auth import views as auth
from django.conf.urls.static import static
from django.contrib.auth.views import LogoutView
urlpatterns = [
    path('', views.home, name="home"),
]
