from django.urls import path
from . import views
urlpatterns = [
    path("" , views.hello_world, name="hello_world"),
    path("about/" , views.about, name="about" ),
    path("login/" , views.login_user, name="login"),
    path("logout/" , views.logout_user, name="logout"),
]
