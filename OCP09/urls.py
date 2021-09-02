"""OCP09 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from create_review.views import create_review_view
from store.login_views import login_view
from store.logout_views import logout_view
from store.register_views import register_view
from store.welcome_views import welcome_screen
from subscribe.followed_user import followed_users
from subscribe.views import subscribe_view, un_follow
from ticket.views import create_ticket_view, tickets_view, delete_ticket

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", welcome_screen),
    path("login/", login_view),
    path("register/", register_view),
    path("logout/", logout_view),
    path("subscribe/", subscribe_view),
    path("followed_users/", followed_users),
    path("unfollow/", un_follow),
    path("create_ticket/", create_ticket_view),
    path("create_review/", create_review_view),
    path("tickets/", tickets_view),
    path("delete_ticket/", delete_ticket),
]
