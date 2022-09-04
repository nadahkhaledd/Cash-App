from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.models import User
from .forms import TransferForm
from .models import Account

def profile(request, username):
    user = User.objects.get(username=username)
    account = user.account_set.all()[0]
    return render(request, 'profile.html', {'user': user, 'account': account})


def transfer(request):
    if request.method == "POST":
        form = TransferForm(request.POST)
        if form.is_valid():
            if (Account.confirm_transfer(form.data['amount'], form.data['receiver_account_number'],
                                     form.data['sender'])):
                return HttpResponseRedirect('/')
    else:
        form = TransferForm()
    return render(request, 'transfer.html', {"form": form})

