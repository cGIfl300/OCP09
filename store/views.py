from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect


@login_required
def welcome_screen(request):
    return render(request, "welcome_screen.html")


def logout_view(request):
    # Just logout
    logout(request)
    return redirect("/")


def login_view(request):
    # if this is a POST request we need to process the form data
    if request.method == "POST":
        user = authenticate(
            username=request.POST.get("username", None),
            password=request.POST.get("password", None),
        )
        if user is not None:
            login(request, user)
            # Redirect to a success page.
            return render(request, "success_identify.html")
        else:
            # 'invalid login'
            return render(request, "login.html")

    # if a GET (or any other method) we'll create a blank form
    else:
        return render(request, "login.html")

    return render(request, "login.html")


def register_view(request):
    # if this is a POST request we need to process the form data
    if request.method == "POST":
        # Here will be the code
        username = request.POST.get("username", None)
        password1 = request.POST.get("password1", None)
        password2 = request.POST.get("password2", None)

        if password1 == password2:
            password = password1
        else:
            password = None

        user = authenticate(
            username=username,
            password=password,
        )
        if user is not None:
            login(request, user)
            # If user already exist, redirect to the login page.
            return redirect("/login/")
        else:
            # Create the user.

            # Check if the username already is in our database
            # If True, return to the login page.
            # Else Create the user
            # Return a success page

            # Follow just for DEBUG
            return render(request, "success_create.html")

    return render(request, "register.html")
