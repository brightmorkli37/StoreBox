from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import NewUserForm
from project_root.settings import *
from .models import Payment


def index(request):

    template_name = 'accounts/index.html'
    context = {}
    return render(request, template_name, context)

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('storage:dashboard')
           
        else:
            return render(request, 'accounts/login.html', {'message': 'login failed, please try again'})
    else:
        return render(request, 'accounts/login.html')


def user_signup(request):
    form = NewUserForm()
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful." )
            return redirect("storage:dashboard")
        else:
            messages.error(request, "Unsuccessful registration. Invalid information.")
            form = NewUserForm()
	
    template_name = 'accounts/register.html'
    context = {"form": form}
    return render(request, template_name, context)

def pricing(request):

    template_name = 'accounts/pricing.html'
    context = {
        'paystack_public_key': PAYSTACK_PUBLIC_KEY,

    }
    return render(request, template_name, context)

def payment(request, ref, amount):
    payment = ref

    dues_payment = Payment.objects.create(
        user = request.user,
        amount = amount,
        ref = ref,
        email = request.user.email,
        verified = True,
    )
    return redirect('storage:dashboard')


def user_logout(request):
    logout(request)
    return redirect(reverse('accounts:index'))