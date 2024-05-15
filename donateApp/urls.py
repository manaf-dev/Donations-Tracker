from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    # path('events/', views.eventsList, name='events'),
    # path('event/<slug:slug>/', views.eventDetail, name='event-detail'),
    path('<slug:slug>/totalamount/', views.eventAmount, name='amount'),
    path('<slug:slug>/donors/', views.eventDonors, name='donors'),
    path('<slug:slug>/donate/', views.donate, name='donate'),
    path('<slug:slug>/save-donation/', views.donateSave, name='save-donate'),
    path('create-event/', views.createEvent, name='create-event'),
    path('delete-event/<slug:slug>/', views.deleteEvent, name='delete-event'),
    path('event-state/<slug:slug>/', views.eventState, name='event-state'),

    path('events/', views.EventList.as_view(), name='events'),
    path('event/<slug:slug>/', views.EventDetail.as_view(), name='event-detail'),
]