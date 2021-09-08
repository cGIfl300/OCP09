from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db import transaction
from django.shortcuts import render

from store.models import Ticket, Review
from ticket.stars import stars


@login_required
@transaction.atomic
def create_review_view(request):
    # Get actual user
    actual_user = User.objects.filter(username__iexact=request.user.username)[0]

    # if this is a POST request we need to process the form data
    if request.method == "POST":
        ticket_title = request.POST.get("ticket_title", None)
        ticket_description = request.POST.get("ticket_description", None)
        ticket_picture = request.POST.get("ticket_picture", None)
        review_rating = request.POST.get("review_rating", None)
        review_headline = request.POST.get("review_headline", None)
        review_body = request.POST.get("review_body", None)

        if (
                ticket_title is not None
                and ticket_description is not None
                and review_rating is not None
        ):
            # Redirect to a success page
            context = {
                "ticket_title": ticket_title,
                "ticket_description": ticket_description,
                "ticket_picture": ticket_picture,
                "review_rating": stars(int(review_rating), 5),
                "review_headline": review_headline,
                "review_body": review_body,
            }
            new_ticket = Ticket(
                user=actual_user,
                title=ticket_title,
                description=ticket_description,
                image=ticket_picture,
            )
            new_ticket.save()
            new_review = Review(
                user=actual_user,
                ticket=new_ticket,
                rating=int(review_rating),
                headline=review_headline,
                body=review_body,
            )
            new_review.save()
            return render(request, "success_review.html", context)

    return render(request, "create_review.html")
