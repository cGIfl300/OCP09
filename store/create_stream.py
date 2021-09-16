#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright(C) 2021 cGIfl300 <cgifl300@gmail.com>
from store.models import Ticket, Review, UserFollows
from ticket.stars import stars


def create_stream(local_user):
    """
    Create a global stream for a defined user
    :param local_user: actual User
    :return: ordered list of things
    """
    articles = []
    tmp_review = None

    user_tickets = Ticket.objects.filter(user=local_user)
    user_reviews = Review.objects.filter(user=local_user)

    # Get the USER tickets
    for user_ticket in user_tickets:
        user_review = Review.objects.filter(user=local_user,
                                            ticket=user_ticket).first()
        if user_review:
            user_review.stars = stars(user_review.rating, 5)
        user_ticket.review = user_review
        articles.append(user_ticket)

    # Get the USER reviews
    for user_review in user_reviews:
        user_review.stars = stars(user_review.rating, 5)
        articles.append(user_review)

    # For each user we follow, chek his reviews and tickets
    users_follow = UserFollows.objects.filter(user=local_user.id)
    for follower in users_follow:
        # Get the follower tickets and reviews
        user_tickets = Ticket.objects.filter(user=follower.followed_user)
        user_reviews = Review.objects.filter(user=follower.followed_user)

        # Get the tickets
        for user_ticket in user_tickets:
            user_review = Review.objects.filter(user=follower.followed_user,
                                                ticket=user_ticket).first()
            if user_review:
                user_review.stars = stars(user_review.rating, 5)
            user_ticket.review = user_review
            articles.append(user_ticket)

        # Get the reviews
        for user_review in user_reviews:
            user_review.stars = stars(user_review.rating, 5)
            articles.append(user_review)

    articles = reversed(
        sorted(articles, key=lambda article_tmp: article_tmp.time_created)
    )
    return articles
