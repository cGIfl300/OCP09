from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from .form_login import LoginForm


@login_required
def welcome_screen(request):
    return render(request, "welcome_screen.html")


def login_screen(request):
    # if this is a POST request we need to process the form data
    if request.method == "POST":
        # create a form instance and populate it with data from the request:
        form = LoginForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data["username"],
                password=form.cleaned_data["password"],
            )
            if user is not None:
                login(request, user)
                # Redirect to a success page.
                return render(request, "success.html")
            else:
                # Return an 'invalid login' error message.
                form = LoginForm()

    # if a GET (or any other method) we'll create a blank form
    else:
        form = LoginForm()

    return render(request, "login.html", {"LoginForm": LoginForm})
