#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright(C) 2021 cGIfl300 <cgifl300@gmail.com>
from django.contrib.auth.models import User

from store.models import Ticket, Review


def already_commented(ticket_id, username):
    """
    check if a ticket has already been commented
    :param ticket_id: ticket id
    :param username: actual username
    :return:
    """
    # Get actual user
    actual_user = User.objects.filter(username__iexact=username).first()
    actual_ticket = Ticket.objects.filter(id=ticket_id).first()

    review = Review.objects.filter(user=actual_user,
                                   ticket=actual_ticket).first()
    if review is None:
        return False
    return True
