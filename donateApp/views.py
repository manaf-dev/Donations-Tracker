from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import ListView, DetailView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Sum

from .models import Event, Donor, Donation
from .forms import CreateEventForm


# Create your views here.
@login_required
def home(request):
    completed_events = Event.objects.filter(admin=request.user, is_completed=True).count()
    uncompleted_events = Event.objects.filter(admin=request.user, is_completed=False).count()

    visit_count = request.session.get('visits', 0)
    request.session['visits'] = visit_count + 1
    visit_count = request.session['visits']

    context = {'comp_events':completed_events, 'uncomp_events':uncompleted_events, 'visit_count':visit_count}
    return render(request, 'donateApp/index.html', context)


@login_required
def eventsList(request):
    events = Event.objects.filter(admin=request.user)
    context = {'events':events}
    return render(request, 'donateApp/event_list.html', context)

@login_required
def eventDetail(request, slug):
    event = Event.objects.get(slug=slug)
    donations = event.donations.all()
    total_amount = donations.aggregate(Sum('amount'))['amount__sum']
    if total_amount is None:
        total_amount = '0.00'
    donors = donations.values('donor').distinct().count()
    context = {'event':event, 'total_amount':total_amount, 'donors':donors}
    return render(request, 'donateApp/event_detail.html', context)


@login_required
def eventAmount(request, slug):
    event = Event.objects.get(slug=slug)
    donations = event.donations.filter(event=event)
    total_amount = donations.aggregate(Sum('amount'))['amount__sum']
    if total_amount is None:
        total_amount = '0.00'
    context = {'event':event, 'total_amount':total_amount}
    return render(request, 'donateApp/amount.html', context)


@login_required
def eventDonors(request, slug):
    event = Event.objects.get(slug=slug)
    donations = event.donations.filter(event=event)
    context = {'event':event, 'donations':donations}
    return render(request, 'donateApp/donors.html', context)


def donate(request, slug):
    event = Event.objects.get(slug=slug)
    context = {'event':event}
    return render(request, 'donateApp/donate.html', context)


def donateSave(request, slug):
    event = Event.objects.get(id=slug)
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        amount = request.POST.get('amount')
        donor = Donor.objects.create(name=name, phone_num=phone)
        Donation.objects.create(event=event, donor=donor, amount=amount)
        return redirect('donate', slug=event.slug)
    return redirect('donate', pk=event.id)



def createEvent(request):
    form = CreateEventForm()
    if request.method == 'POST':
        form = CreateEventForm(request.POST, request.FILES)
        if form.is_valid():
            event = form.save(commit=False)
            event.admin = request.user
            event.save()
            return redirect('events')
    context = {'form': form}
    return render(request, 'donateApp/create_event.html', context)


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

