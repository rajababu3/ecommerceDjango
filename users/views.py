from django.shortcuts import render, HttpResponseRedirect, reverse,Http404
from django.contrib.auth import login,logout,authenticate
from .forms import LoginForm, RegistrationForm,UserAddressForm
# Create your views here.

def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/')

def login_view(request):
    form = LoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user = authenticate(username= username, password=password)
        login(request, user)
        return HttpResponseRedirect("/cart/")
    context = {
        "form": form
    }
    return render(request, "forms.html", context)


def registration_view(request):

    form = RegistrationForm(request.POST or None)
    if form.is_valid():
        print("Valid")
        new_user = form.save(commit=False)
        new_user.save()
        return HttpResponseRedirect("/users/login")
        # username = form.cleaned_data['username']
        # password = form.cleaned_data['password']
        # user = authenticate(username= username, password=password)
        # login(request, user)
    context = {
        "form": form
    }

    return render(request, "forms.html", context)


def add_user_address(request):

    form = UserAddressForm(request.POST or None)
    if form.is_valid():
        new_address = form.save(commit=False)
        new_address.user = request.user
        new_address.save()
    context = {
        "form": form
    }
    return render(request, "orders/shipping.html", context)