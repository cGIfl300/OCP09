#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright(C) 2021 cGIfl300 <cgifl300@gmail.com>
from django.contrib.auth import authenticate, login
from django.shortcuts import render


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
