from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import TransferForm
from .models import Account, Transaction


@login_required
def profile(request):
    username = request.user.username
    user = User.objects.filter(username=username)[0]
    account = user.account_set.all()[0]
    transactions = reversed(Transaction.objects.filter(receivant=account, type='D')[:10])
    return render(request, 'profile.html', {'user': user, 'account': account, 'transactions': transactions})


def transfer(request):
    if request.method == "POST":
        form = TransferForm(request.POST)
        if form.is_valid():
            if Account.confirm_transfer(form.data['amount'], form.data['receiver_account_number'],
                                        request.user.account_set.all()[0]):

                return HttpResponseRedirect('/')
    else:
        form = TransferForm()
    return render(request, 'transfer.html', {"form": form})
