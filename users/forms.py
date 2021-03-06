from django import forms
from django.contrib.auth.models import User
from .models import UserProfile, UserContact


class UserAddressForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['firstName', 'lastName', 'mobile','address','address2','city','state','zipCode','country','billing']


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput())

    def clean_username(self):
        username = self.cleaned_data.get("username")

        try:
            user = User.objects.get(username= username)
        except User.DoesNotExist:
            raise forms.ValidationError("Are you sure you are Registered? ")
        return username

    def clean_password(self):
        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")

        try:
            user = User.objects.get(username=username)
        except:
            user = None

        if user is not None and not user.check_password(password):
            raise forms.ValidationError("Invalid Password")
        elif user is None:
            pass
        else:
            return password


class RegistrationForm(forms.ModelForm):
    password1 = forms.CharField(label="Password", widget=forms.PasswordInput())
    password2 = forms.CharField(label="Confirm Password", widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ['username', 'email']

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")

        try:
            if ((password1 and password2) and (password1 != password2)):
                raise forms.ValidationError("Password Do not Match")
        except:
            pass
        return password2

    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        if commit:
            user.save()
        return user


class UserContactForm(forms.ModelForm):
    class Meta:
        model = UserContact
        fields = ['name', 'email', 'subject','message']









