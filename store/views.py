from django.shortcuts import redirect


def stream_view(request):
    # Here will be the view "Flux"
    return redirect("/")


def create_ticket_view(request):
    # Here will be the view "Ticket"
    return redirect("/")


def create_comment_view(request):
    # Here will be the view "Critique"
    return redirect("/")


def reply_comment_view(request):
    # Here will be the view "Reply to a critique"
    return redirect("/")


def my_stream_view(request):
    # Here will be the view "Voir vos propres post"
    return redirect("/")


def edit_comment_view(request):
    # Here will be the view "Modifier votre propre critique"
    return redirect("/")


def edit_ticket_view(request):
    # Here will be the view "Modifier votre propre ticket"
    return redirect("/")
