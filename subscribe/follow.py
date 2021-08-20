#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright(C) 2021 cGIfl300 <cgifl300@gmail.com>
from django.contrib.auth.models import User
from django.db import IntegrityError

from store.models import UserFollows


def follow(user_to_follow, request):
    # Get actual user
    actual_user = User.objects.filter(username__iexact=request.user.username)[0]

    # Get user to follow
    user_to_follow = User.objects.filter(username__iexact=user_to_follow)[0]

    try:
        add_followed = UserFollows(user=actual_user,
                                   followed_user=user_to_follow)
        add_followed.save()
    except IntegrityError:
        # If user is already followed, just return True
        return False
    return True
