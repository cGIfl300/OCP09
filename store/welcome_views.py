#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright(C) 2021 cGIfl300 <cgifl300@gmail.com>
from django.contrib.auth.decorators import login_required
from django.shortcuts import render


@login_required
def welcome_screen(request):
    return render(request, "welcome_screen.html")
