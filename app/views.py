from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.models import User
from .models import Account

def index(request):
    return HttpResponse('Hello')

def profile(request, username):
    user = User.objects.get(username=username)
    accounts = user.account_set.all()
    return render(request, 'profile.html', {'user': user, 'accounts': accounts})


def transfer(request):
    if request.method == "POST":
        pass
    return render(request, 'transfer.html', {"data": 'DrinkForm'})

