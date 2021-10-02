from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db import transaction
from django.shortcuts import render
from django.utils.datastructures import MultiValueDictKeyError

from store.models import Ticket, Review
from store.refresh_static_files import refresh_static_files
from ticket.stars import stars


@login_required
@transaction.atomic
def ticket_review_view(request):
    # Create a ticket and it's review one click

    # Get actual user
    actual_user = User.objects.filter(username__iexact=request.user.username)[0]

    # if this is a POST request we need to process the form data
    if request.method == "POST":
        ticket_title = request.POST.get("ticket_title", None)
        ticket_description = request.POST.get("ticket_description", None)
        # Check if a file has been sent
        try:
            ticket_picture = request.FILES["ticket_image"]
        except MultiValueDictKeyError:
            ticket_picture = None
        review_rating = request.POST.get("review_rating", None)
        review_headline = request.POST.get("review_headline", None)
        review_body = request.POST.get("review_body", None)

        if (
                ticket_title is not None
                and ticket_description is not None
                and review_rating is not None
        ):
            # Redirect to a success page
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
            context = {
                "ticket_title": ticket_title,
                "ticket_description": ticket_description,
                "ticket_picture": ticket_picture,
                "review_rating": stars(int(review_rating), 5),
                "review_headline": review_headline,
                "review_body": review_body,
                "ticket": new_ticket,
            }
            return render(request, "success_review.html", context)

    return render(request, "ticket_review_one_click.html")
