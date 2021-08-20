from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.shortcuts import render

from store.models import UserFollows


@login_required
def subscribe_view(request):
    followed_users_list = followed_users(request)
    users_who_follow = who_is_following(request)

    # if this is a POST request we need to process the form data
    if request.method == "POST":
        user_to_follow = request.POST.get("user_to_follow", None),

        # if there is an user to follow, then follow he / she
        if user_to_follow is not None:
            # User to follow
            user_to_follow = user_to_follow[0]

            if user_exist(user_to_follow):
                if follow(
                        user_to_follow,
                        request):
                    # User successfully added
                    return render(request, "follow_success.html",
                                  {"user_to_follow": user_to_follow,
                                   "who_is_following": users_who_follow})
                else:
                    # User ever followed
                    return render(request, "ever_followed.html",
                                  {"user_to_follow": user_to_follow,
                                   "who_is_following": users_who_follow})
            else:
                return render(request, "user_doesnt_exist.html")

    # if a GET (or any other method) we'll create a blank form
    else:
        return render(request, "subscribe.html",
                      {"followed_users": followed_users_list,
                       "who_is_following": users_who_follow})

    return render(request, "subscribe.html",
                  {"followed_users": followed_users_list,
                   "who_is_following": users_who_follow})


def followed_users(request):
    # Get actual user
    actual_user = User.objects.filter(username__iexact=request.user.username)[0]

    # Get users list
    return UserFollows.objects.filter(user=actual_user)


def user_exist(user_to_follow):
    if User.objects.filter(username__iexact=user_to_follow):
        return True
    return False


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


@login_required
def un_follow(request):
    # Get actual user
    actual_user = User.objects.filter(username__iexact=request.user.username)[0]

    # if this is a POST request we need to process the form data
    if request.method == "POST":
        user_to_unfollow = request.POST.get("user_to_unfollow", None),

        # if there is an user to unfollow, then unfollow he / she
        if user_to_unfollow is not None:
            user_to_unfollow = user_to_unfollow[0]
            # Get user to unfollow (object)
            object_user_to_unfollow = \
                User.objects.filter(username__iexact=user_to_unfollow)[0]
            UserFollows.objects.filter(user=actual_user,
                                       followed_user=object_user_to_unfollow).delete()
            return render(request, "unfollow.html",
                          {"user_to_unfollow": user_to_unfollow})
