from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render

from store.models import UserFollows
from subscribe.follow import follow
from subscribe.followed_user import followed_users
from subscribe.user_exist import user_exist
from subscribe.who_is_following import who_is_following


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
