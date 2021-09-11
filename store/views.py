from django.shortcuts import redirect


def my_stream_view(request):
    # Here will be the view "Voir vos propres post"
    return redirect("/")


def edit_comment_view(request):
    # Here will be the view "Modifier votre propre critique"
    return redirect("/")


def edit_ticket_view(request):
    # Here will be the view "Modifier votre propre ticket"
    return redirect("/")
