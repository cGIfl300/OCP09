#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright(C) 2021 cGIfl300 <cgifl300@gmail.com>
from django.contrib.auth import logout
from django.shortcuts import redirect


def logout_view(request):
    # Just logout
    logout(request)
    return redirect("/")
