from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import ContactForm, SampleForm, LoginForm, RegisterForm
from django.contrib.auth import authenticate, login


def home_page(request):
    return render(request, "home_page.html", {
        "title": "This is a simple Headline",
    })

def contact_page(request):
    contact_form = ContactForm(request.POST or None)
    sample_form = SampleForm()
    if request.method == "POST":
        # print(request.POST)
        # print(request.POST.get('some_text_value'))
        # print(request.POST.get('fullname'))
        # print(request.POST.get('email'))
        # print(request.POST.get('content'))

        if contact_form.is_valid():
            print(contact_form.cleaned_data.get('fullname'))
    return render(request, "contact_view.html", {
        "contact_form" : contact_form,
        "sample_form": sample_form,
    })

def login_page(request):
    login_form = LoginForm(request.POST or None)
    if login_form.is_valid():
        username = login_form.cleaned_data.get("username")
        password = login_form.cleaned_data.get("password")
        print(username, password)
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # Redirect to a success page.
            print("Logged In")
            return redirect("home")
        else:
            print("Not LoggedIn")
    return render(request, "login_page.html", {
        "login_form": login_form,
    })

def register_page(request):
    register_form = RegisterForm(request.POST or None)
    if register_form.is_valid():
        print(register_form.cleaned_data)
    context = {
        "register_form": register_form,
    }
    return render(request, "register_page.html", context)

def home_page_old00(request):
    return render(request, "home_page.html")

def home_page_old(request):
    html_ = """
    <!doctype html>
    <html lang="en">
      <head>
        <!-- Required meta tags -->
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    
        <!-- Bootstrap CSS -->
        <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.1.3/css/bootstrap.min.css" integrity="sha384-MCw98/SFnGE8fJT3GXwEOngsV7Zt27NXFoaoApmYm81iuXoPkFOJwJ8ERdknLPMO" crossorigin="anonymous">
    
        <title>Hello, world!</title>
      </head>
      <body>
        <h1 class="text-center mt-5">Hello, world!</h1>
    
        <!-- Optional JavaScript -->
        <!-- jQuery first, then Popper.js, then Bootstrap JS -->
        <script src="https://code.jquery.com/jquery-3.3.1.slim.min.js" integrity="sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo" crossorigin="anonymous"></script>
        <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.3/umd/popper.min.js" integrity="sha384-ZMP7rVo3mIykV+2+9J3UJ46jBk0WLaUAdn689aCwoqbBJiSnjAK/l8WvCWPIPm49" crossorigin="anonymous"></script>
        <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.1.3/js/bootstrap.min.js" integrity="sha384-ChfqqxuZUCnJSK3+MXmPNIyE6ZbWh2IMqE241rYiqJxyMiZ6OW/JmZQ5stwEULTy" crossorigin="anonymous"></script>
      </body>
    </html>
    """
    return HttpResponse(html_)


