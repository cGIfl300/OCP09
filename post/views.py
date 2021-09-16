from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render

# Create your views here.
from post.create_stream_post import create_stream_post


@login_required
def post_view(request):
    # Get actual user
    actual_user = User.objects.filter(username__iexact=request.user.username)[0]
    context = {"articles": create_stream_post(local_user=actual_user)}
    return render(request, "post_view.html", context)
