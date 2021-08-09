#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright(C) 2021 cGIfl300 <cgifl300@gmail.com>
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.shortcuts import redirect, render


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
            user = User.objects.create_user(
                username=username, email="not@needed.com", password=password
            )
            login(request, user)

            return render(request, "success_create.html")

    return render(request, "register.html")
