#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright(C) 2021 cGIfl300 <cgifl300@gmail.com>
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render

from store.create_stream import create_stream


@login_required
def welcome_screen(request):
    # Get actual user
    actual_user = User.objects.filter(username__iexact=request.user.username)[0]

    create_stream(local_user=actual_user)
    return render(request, "welcome_screen.html")
