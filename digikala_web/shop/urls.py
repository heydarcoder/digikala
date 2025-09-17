from django.urls import path
from . import views
urlpatterns = [
    path("" , views.hello_world, name="hello_world"),
    path("about/" , views.about, name="about" ),
    path("login/" , views.login_user, name="login"),
    path("logout/" , views.logout_user, name="logout"),
    path("signup/", views.signup_user, name="signup"),
    path("signup/", views.signup_user, name="signup"),
    path("products/<int:pk>", views.products, name="products"),
]
