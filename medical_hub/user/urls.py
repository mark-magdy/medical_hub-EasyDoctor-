from django.urls import path, include
from django.conf import settings
from . import views
from django.contrib.auth import views as auth
from django.conf.urls.static import static
# from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', views.landing, name="landing"),
    path('done', views.done, name="done"),
    path('mylogout', views.mylogout,name="mylogout")
    # path("logout/", LogoutView.as_view(), name="logout"),
    # path(
    #     "logout/",
    #     auth.LogoutView.as_view(template_name="welcome.html"),
    #     name="logout",
    # ),
]
