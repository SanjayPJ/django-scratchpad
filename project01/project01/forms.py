from django import forms
from django.contrib.auth import get_user_model

class ContactForm(forms.Form):
    fullname = forms.CharField(max_length=100, widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Enter fullname"}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={"class": "form-control", "placeholder": "Enter Your Email"}))
    content = forms.CharField(widget=forms.Textarea(attrs={"class": "form-control", "value": "Enter some text"}))

    def clean_email(self):
        email = self.cleaned_data.get("email")
        if not "gmail.com" in email:
            raise forms.ValidationError("Email Must be Gmail")
        return email

class SampleForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    address_1 = forms.CharField(widget=forms.Textarea)
    address_2 = forms.CharField(widget=forms.Textarea)

    # assigning class to the form elements
    name.widget.attrs.update({'class': 'form-control'})
    email.widget.attrs.update({'class': 'form-control'})
    address_1.widget.attrs.update({'class': 'form-control'})
    address_2.widget.attrs.update({'class': 'form-control'})

class LoginForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(max_length=100, widget=forms.PasswordInput)

    # class
    username.widget.attrs.update({"class": "form-control"})
    password.widget.attrs.update({"class": "form-control"})

User = get_user_model()

class RegisterForm(forms.Form):
    username = forms.CharField(max_length=100)
    email = forms.EmailField()
    password = forms.CharField(max_length=100, widget=forms.PasswordInput)
    password2 = forms.CharField(max_length=100, widget=forms.PasswordInput, label="Confirm Password")

    # class
    username.widget.attrs.update({"class": "form-control"})
    email.widget.attrs.update({"class": "form-control"})
    password.widget.attrs.update({"class": "form-control"})
    password2.widget.attrs.update({"class": "form-control"})

    def clean_email(self):
        email = self.cleaned_data.get("email")
        qs = User.objects.filter(email=email)
        if qs.exists():
            raise forms.ValidationError("Email is taken")
        return email

    def clean_username(self):
        username = self.cleaned_data.get("username")
        qs = User.objects.filter(username=username)
        if qs.exists():
            raise forms.ValidationError("Username is taken")
        return username


    def clean(self):
        password = self.cleaned_data.get("password")
        password2 = self.cleaned_data.get("password2")

        if password != password2:
            raise forms.ValidationError("Passwords Must Match")
        return self.cleaned_data


