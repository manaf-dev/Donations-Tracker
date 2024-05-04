from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, DetailView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Sum

from .models import Event, Donor, Donation

# Create your views here.
# @login_required
def home(request):
    completed_events = Event.objects.filter(admin=request.user, is_completed=True).count()
    uncompleted_events = Event.objects.filter(admin=request.user, is_completed=False).count()

    context = {'comp_events':completed_events, 'uncomp_events':uncompleted_events}
    return render(request, 'donateApp/index.html', context)


# @login_required
def eventsList(request):
    events = Event.objects.filter(admin=request.user)
    context = {'events':events}
    return render(request, 'donateApp/event_list.html', context)

# @login_required
def eventDetail(request, pk):
    event = Event.objects.get(id=pk)
    donations = event.donations.all()
    total_amount = donations.aggregate(Sum('amount'))['amount__sum']
    donors = donations.values('donor').distinct().count()
    context = {'event':event, 'total_amount':total_amount, 'donors':donors}
    return render(request, 'donateApp/event_detail.html', context)


# @login_required
def eventAmount(request, pk):
    event = Event.objects.get(id=pk)
    donations = event.donations.filter(event=event)
    total_amount = donations.aggregate(Sum('amount'))['amount__sum']
    context = {'event':event, 'total_amount':total_amount}
    return render(request, 'donateApp/amount.html', context)


# @login_required
def eventDonors(request, pk):
    event = Event.objects.get(id=pk)
    donations = event.donations.filter(event=event)
    # donors = Donor.objects.filter(id=event)
    context = {'event':event, 'donations':donations}
    return render(request, 'donateApp/donors.html', context)


def donate(request):
    return render(request, 'donateApp/donate.html')

# class EventList(LoginRequiredMixin, ListView):
#     model = Event
#     context_object_name = 'events'
#     template_name='event_list.html'
#     login_url = '/'


# class EventDetail(LoginRequiredMixin, DetailView):
#     model = Event
#     template_name='donateApp/event_detail.html'
#     context_object_name = 'event'
#     login_url = '/'








def create_event(request):
    return render(request, 'donateApp/create_event.html')