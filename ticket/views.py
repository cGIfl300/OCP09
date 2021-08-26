from django.contrib.auth.decorators import login_required
from django.shortcuts import render


@login_required
def create_ticket_view(request):
    return render(request, "create_ticket.html")
