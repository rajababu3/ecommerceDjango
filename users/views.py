from django.shortcuts import render, HttpResponseRedirect, reverse,Http404
from django.contrib.auth import login,logout,authenticate
from .forms import LoginForm, RegistrationForm,UserAddressForm, UserContactForm
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
    loginForm = LoginForm(request.POST or None)
    # btn = "Login"
    if loginForm.is_valid():
        username = loginForm.cleaned_data['username']
        password = loginForm.cleaned_data['password']
        user = authenticate(username=username, password=password)
        login(request, user)
        messages.success(request, "Successfully Logged In. Welcome Back!")
        return HttpResponseRedirect("/")
    context = {
        "loginForm": loginForm,
        # "submit_btn": btn,
    }
    return render(request, "account/login.html", context)


def registration_view(request):
    registerForm = RegistrationForm(request.POST or None)
    # btn = "Join"
    if registerForm.is_valid():
        new_user = registerForm.save(commit=False)
        new_user.save()
        messages.success(request, "Successfully Registered.")
        return HttpResponseRedirect("/")

    context={
        "registerForm": registerForm,
        # "submit_btn": btn,
    }
    return render(request, "account/register.html", context)

def contact_view(request):
    contactForm = UserContactForm(request.POST or None)
    # btn = "Join"
    if contactForm.is_valid():
        new_user = contactForm.save(commit=False)
        new_user.save()
        messages.success(request, "Successfully Registered.")
        return HttpResponseRedirect("/")

    context = {
        "contactForm": contactForm,
        # "submit_btn": btn,
    }
    return render(request, "contact.html", context)

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

def thankyou_view(request):
    template = 'account/thankyou.html'
    context = {}
    return render(request,template, context)