#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright(C) 2021 cGIfl300 <cgifl300@gmail.com>
from django.contrib.auth.models import User


def user_exist(user_to_follow):
    if User.objects.filter(username__iexact=user_to_follow):
        return True
    return False
