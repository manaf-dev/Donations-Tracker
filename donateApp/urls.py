from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('events/', views.eventsList, name='events'),
    path('event/<int:pk>/', views.eventDetail, name='event-detail'),
    path('event/<int:pk>/totalamount/', views.eventAmount, name='amount'),
    path('event/<int:pk>/donors/', views.eventDonors, name='donors'),
    path('donate/<int:pk>/', views.donate, name='donate'),
    path('collect-donation/<int:pk>/', views.donateSave, name='save-donate'),
    path('create-event/', views.createEvent, name='create-event'),
]