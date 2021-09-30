from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect

from store.models import Review, Ticket


@login_required
def delete_review(request):
    """
    delete a ticket as needed
    """
    if request.method == "GET":
        ticket_id = request.GET.get("ticket_id", None)
        if ticket_id:
            selected_ticket = Ticket.objects.filter(id=ticket_id).first()
            selected_review = Review.objects.filter(
                ticket=selected_ticket).first()
            selected_review.delete()
    return redirect("/")
