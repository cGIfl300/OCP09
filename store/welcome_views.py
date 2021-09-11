#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright(C) 2021 cGIfl300 <cgifl300@gmail.com>
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render

from store.models import Ticket, Review, UserFollows
from ticket.stars import stars


@login_required
def welcome_screen(request):
    # Get actual user
    actual_user = User.objects.filter(username__iexact=request.user.username)[0]

    create_stream(local_user=actual_user)
    return render(request, "welcome_screen.html")


def create_stream(local_user):
    """
    Create a global stream for a defined user
    :param local_user: actual User
    :return: ordered list of things
    """
    articles = []
    tmp_review = None

    # Obtain the list of ticket created by actual user
    user_tickets = list(Ticket.objects.filter(user=local_user))

    # For each ticket, check if there is a review wrote by the actual user
    for ticket in user_tickets:
        tpm_review = Review.objects.filter(ticket=ticket).first()
        tmp_review.stars = stars(
            number_of_stars=int(tmp_review.rating), max_stars=5
        )
        if tpm_review is not None:
            ticket.review = tmp_review
            tmp_review = None
        articles.append(ticket)

    users_follow = list(UserFollows.objects.filter(user=local_user))

    # For each user we follow, chek his reviews and tickets
    for follower in users_follow:
        print(f"{follower} is following you.")
        # Get the user identify
        user_tickets = Ticket.objects.filter(user=follower.user)
        user_reviews = Review.objects.filter(user=follower.user)

        if user_tickets is not None:
            articles = articles + list(user_tickets)
            user_tickets = None
        if user_reviews is not None:
            articles = articles + list(user_reviews)
            user_reviews = None

    articles = reversed(
        sorted(articles, key=lambda article_tmp: article_tmp.time_created)
    )

    return articles
