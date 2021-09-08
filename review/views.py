from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import redirect

from store.models import Ticket, Review
from ticket.already_commented import already_commented


@login_required
def update_review(request):
    """
    Create or update a review
    :param request: ticket_id - The ticket ID (get)
    :return:
    """
    # Get params from the form (rating, headline, body)

    ticket_id = request.GET.get("ticket_id", None)
    actual_user = User.objects.filter(username=request.user.username).first()

    rating = request.POST.get("review_rating", None)
    headline = request.POST.get("review_headline", None)
    body = request.POST.get("review_body", None)

    if rating is None or headline is None or body is None or ticket_id is None:
        return redirect("/review_from_tickets/")

    ticket_id = int(ticket_id)
    rating = int(rating)

    # Check if a review is already existing
    if already_commented(ticket_id=ticket_id, username=request.user.username):
        # True: update the review
        actual_ticket = Ticket.objects.filter(id=ticket_id).first()

        review = Review.objects.filter(
            user=actual_user, ticket=actual_ticket
        ).first()
        review.headline = headline
        review.rating = rating
        review.body = body
        review.save()
    else:
        # False: create the review
        review = Review(
            headline=headline,
            rating=rating,
            body=body,
            ticket=Ticket(id=ticket_id),
            user=actual_user,
        )
        review.save()

    # Return a success page
    return redirect("/")
