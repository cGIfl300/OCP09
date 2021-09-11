#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright(C) 2021 cGIfl300 <cgifl300@gmail.com>
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render

from store.models import Ticket, Review, UserFollows


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
    user_tickets = Ticket.objects.filter(user=local_user)

    # For each ticket, check if there is a review wrote by the actual user
    for actual_ticket in user_tickets:

        ### !!! BUG !!! ###

        # Starting development server at http://127.0.0.1:8000/
        # Quit the server with CTRL-BREAK.
        # tmp_review None
        # tmp_review None
        # tmp_review None
        # tmp_review None
        # UserFollows object (7) is following you.
        # [11/Sep/2021 10:39:06] "GET / HTTP/1.1" 200 1972
        # UserFollows object (4) is following you.
        # 2021-09-11 07:27:44.397853+00:00
        # 2021-09-11 07:27:44.397853+00:00
        # 2021-09-11 07:27:36.742039+00:00
        # 2021-09-11 07:27:36.742039+00:00
        # 2021-09-09 15:46:25.970713+00:00
        # 2021-09-09 15:46:25.970713+00:00
        # 2021-09-09 12:27:26.442490+00:00
        # 2021-09-09 12:27:26.442490+00:00
        # 2021-09-09 12:27:26.442490+00:00
        # 2021-09-09 12:24:13.620784+00:00
        # 2021-09-09 12:24:13.620784+00:00
        # 2021-09-09 12:24:13.620784+00:00
        # 2021-09-09 10:48:38.953961+00:00
        # 2021-09-09 10:48:38.953961+00:00
        # 2021-09-09 10:48:38.953961+00:00
        # 2021-09-08 16:05:08.878780+00:00
        # 2021-09-08 16:05:08.878780+00:00
        # 2021-08-26 15:38:14.230213+00:00
        # 2021-08-26 15:38:14.230213+00:00
        # 2021-08-26 15:38:14.230213+00:00

        tpm_review = Review.objects.filter(ticket=actual_ticket,
                                           user=local_user).first()

        if tpm_review is not None:
            actual_ticket.review = tmp_review
            print(f"tmp_review {tmp_review}")
            tmp_review = None

        articles.append(actual_ticket)

    users_follow = UserFollows.objects.filter(user=local_user)

    ### !!! END BUG !!! ####
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
    for article in articles:
        print(article.time_created)
    return articles
