#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright(C) 2021 cGIfl300 <cgifl300@gmail.com>
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from store.models import Ticket
from ticket.already_commented import already_commented


@login_required
def create_review_from_ticket(request):
    """
    Create a review from a ticket
    :param
    request: ticked_id: the ticket id
    :return:
    """
    ticket_id = request.GET.get("ticket_id", None)
    ticket_for_review = Ticket.objects.filter(id=ticket_id).first()
    message = None

    # Check if a review already exist

    if already_commented(ticket_id=ticket_id,
                         username=request.user.username):
        message = "Review already exist - Will erase the existing one"

    # Warm if already existing

    context = ({"ticket": ticket_for_review,
                "message": message})

    return render(request, "create_review_from_ticket.html", context)
