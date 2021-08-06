from django.contrib.auth.decorators import login_required
from django.shortcuts import render


@login_required(login_url="/admin/")
def welcome_screen(request):
    return render(request, "welcome_screen.html")
