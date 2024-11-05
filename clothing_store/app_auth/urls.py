from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path("register/", views.RegisterCustomer.as_view(), name="register-page"),
    path("login/", views.LoginCustomer.as_view(), name="login-page"),
    path("profile/", views.CustomerProfile.as_view(), name="profile-pae"),
    path("logout/", LogoutView.as_view(), name="logout")
]
