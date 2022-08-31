from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.models import User
from .models import Account

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def homePage(request, username):
    user = User.objects.get(username=username)
    accounts = user.account_set.all()
    return render(request, 'home.html', {'user': user, 'accounts': accounts})

