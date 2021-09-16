from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.utils.datastructures import MultiValueDictKeyError

from store.models import Ticket


@login_required
def create_ticket_view(request):
    # Get actual user
    actual_user = User.objects.filter(username__iexact=request.user.username)[0]

    # if this is a POST request we need to process the form data
    if request.method == "POST":
        ticket_title = request.POST.get("ticket_title", None)
        ticket_description = request.POST.get("ticket_description", None)

        # Check if a file has been sent
        try:
            ticket_picture = request.FILES["ticket_picture"]
        except MultiValueDictKeyError:
            ticket_picture = None

        if ticket_title is not None and ticket_description is not None:
            # Redirect to a success page.
            new_ticket = Ticket(
                user=actual_user,
                title=ticket_title,
                description=ticket_description,
                image=ticket_picture,
            )
            new_ticket.save()
            context = {"ticket": new_ticket}
            return render(request, "success_ticket.html", context)

    return render(request, "create_ticket.html")


@login_required
def tickets_view(request):
    """
    Create a review from a ticket
    :param request: webpage request
    :return: the ticket store
    """
    every_ticket = list(Ticket.objects.all())

    context = {"tickets": every_ticket}
    return render(request, "tickets.html", context)


@login_required
def delete_ticket(request):
    """
    Delete a ticket (mainly for debug purpose)
    :param request: ticket.id the ticket id
    :return:
    """
    ticket_id = request.GET.get("ticket_id", None)
    ticket_to_delete = Ticket.objects.filter(id=ticket_id)
    if request.username == ticket_to_delete.user:
        ticket_to_delete.delete()
    return redirect("/tickets/")
