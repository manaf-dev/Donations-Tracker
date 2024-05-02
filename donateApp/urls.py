from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('events/', views.events, name='events'),
    path('event-detail/', views.event_detail, name='event-detail'),
    path('donate/', views.donate, name='donate'),
    path('amount/', views.amount, name='amount'),
]