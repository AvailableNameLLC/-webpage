from django.shortcuts import render
from main.models import Users, username, passwords

def homepage(response):
    return render(response, "main/homepage.html", {})

def signup(response):
    return render(response, "main/signup.html", {})

def signin(response):
    return render(response, "main/signin.html", {})

def account(response):
    return render(response, "main/account.html", {})

def passreset(response):
    return render(response, "main/passwordreset.html", {})

def dashboard(response):
    return render(response, "main/dashboard.html")