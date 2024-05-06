from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('events/', views.eventsList, name='events'),
    path('event/<slug:slug>/', views.eventDetail, name='event-detail'),
    path('<slug:slug>/totalamount/', views.eventAmount, name='amount'),
    path('<slug:slug>/donors/', views.eventDonors, name='donors'),
    path('<slug:slug>/donate/', views.donate, name='donate'),
    path('<int:pk>/collect-donation/', views.donateSave, name='save-donate'),
    path('create-event/', views.createEvent, name='create-event'),
]