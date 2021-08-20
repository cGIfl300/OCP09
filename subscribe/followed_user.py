#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright(C) 2021 cGIfl300 <cgifl300@gmail.com>
from django.contrib.auth.models import User

from store.models import UserFollows


def followed_users(request):
    # Get actual user
    actual_user = User.objects.filter(username__iexact=request.user.username)[0]

    # Get users list
    return UserFollows.objects.filter(user=actual_user)
