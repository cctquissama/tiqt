"""tiqt URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.contrib.auth import views as auth_views
from tiqt.apps.core import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('ticket/new/', views.NewTicketView.as_view(), name='new_ticket'),
    path('ticket/my/', views.MyTicketsView.as_view(), name='my_tickets'),
    path('ticket/open/', views.OpenTicketsView.as_view(), name='open_tickets'),
    path('ticket/closed/', views.ClosedTicketsView.as_view(), name='closed_tickets'),
    path('ticket/<int:pk>/',
         views.TicketDetailView.as_view(), name='ticket_detail'),
    path('ticket/<int:pk>/update/',
         views.TicketUpdateView.as_view(), name='ticket_update'),
    path('ticket/<int:pk>/accept',
         views.TicketAcceptView.as_view(), name='ticket_accept'),
    path('ticket/<int:pk>/close',
         views.CloseTicketView.as_view(), name='ticket_close'),
    path('ticket/<int:ticket_pk>/comment',
         views.CommentView.as_view(), name='ticket_comment'),
    path('accounts/login/',
         auth_views.LoginView.as_view(redirect_authenticated_user=True),
         name='login'),
    path('accounts/logout', auth_views.LogoutView.as_view(), name='logout'),
    path('admin/', admin.site.urls),
]
