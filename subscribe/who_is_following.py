#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright(C) 2021 cGIfl300 <cgifl300@gmail.com>
from store.models import UserFollows


def who_is_following(request):
    users_following_me = []
    for u in UserFollows.objects.all():
        if u.followed_user.username == request.user.username:
            users_following_me.append(u.user.username)
    # Delete same users
    users_following_me = list(set(users_following_me))
    # Sort the list
    users_following_me.sort()
    return users_following_me
