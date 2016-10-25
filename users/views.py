from django.shortcuts import render, HttpResponseRedirect, reverse,Http404
from django.contrib.auth import login,logout,authenticate
from .forms import LoginForm, RegistrationForm,UserAddressForm
from django.contrib import messages
# Create your views here.

def logout_view(request):
    logout(request)
    messages.success(request, "<strong>Successfully Logged out</strong>. Feel free to <a href='%s'>login</a> again." % (
    reverse("auth_login")), extra_tags='safe, abc')
    messages.warning(request, "There's a warning.")
    messages.error(request, "There's an error.")
    return HttpResponseRedirect('%s' % (reverse("auth_login")))

def login_view(request):
    form = LoginForm(request.POST or None)
    btn = "Login"
    if form.is_valid():
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user = authenticate(username=username, password=password)
        login(request, user)
        messages.success(request, "Successfully Logged In. Welcome Back!")
        return HttpResponseRedirect("/")
    context = {
        "form": form,
        "submit_btn": btn,
    }
    return render(request, "forms.html", context)


def registration_view(request):
    form = RegistrationForm(request.POST or None)
    btn = "Join"
    if form.is_valid():
        new_user = form.save(commit=False)
        new_user.save()
        messages.success(request, "Successfully Registered.")
        return HttpResponseRedirect("/")

    context = {
        "form": form,
        "submit_btn": btn,
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