from django.urls import path
from . import views

urlpatterns = [
    path("", views.homepage, name="homepage"),
    path("signup/", views.signup, name="signup"),
    path("signin/", views.signin, name="signin"),
    path("account_menu", views.account, name="account"),
    path("password_reset", views.passreset, name="passwordreset"),
    path("dashboard", views.dashboard, name="dashboard"),

]