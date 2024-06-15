from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.views.generic import ListView, DetailView, TemplateView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Sum
from django.utils import timezone

from .models import Event, Donor, Donation
from .forms import CreateEventForm
from .utils import send_sms


# Create your views here.

class IndexView(TemplateView):
    template_name = 'donateApp/index.html'



@login_required
def home(request):
    completed_events = Event.objects.filter(admin=request.user, is_completed=True).count()
    uncompleted_events = Event.objects.filter(admin=request.user, is_completed=False).count()

    visit_count = request.session.get('visits', 0)
    request.session['visits'] = visit_count + 1
    visit_count = request.session['visits']

    context = {'comp_events':completed_events, 'uncomp_events':uncompleted_events, 'visit_count':visit_count}
    return render(request, 'donateApp/home.html', context)


# @login_required
# def eventsList(request):
#     events = Event.objects.filter(admin=request.user)
#     context = {'events':events}
#     return render(request, 'donateApp/event_list.html', context)
#class-based view
class EventList(LoginRequiredMixin, ListView):
    context_object_name = 'events'
    template_name='donateApp/event_list.html'
    # login_url = '/'
    def get_queryset(self):
        return Event.objects.filter(admin=self.request.user)



# @login_required
# def eventDetail(request, slug):
#     event = Event.objects.get(slug=slug)
#     donations = event.donations.all()
#     total_amount = donations.aggregate(Sum('amount'))['amount__sum']
#     if total_amount is None:
#         total_amount = '0.00'
#     donors = donations.values('donor').distinct().count()
#     context = {'event':event, 'total_amount':total_amount, 'donors':donors}
#     return render(request, 'donateApp/event_detail.html', context)
#class-based view
class EventDetail(LoginRequiredMixin, DetailView):
    model = Event
    template_name='donateApp/event_detail.html'
    context_object_name = 'event'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        event = self.object
        donations = event.donations.all()
        total_amount = donations.aggregate(Sum('amount'))['amount__sum']
        if total_amount is None:
            total_amount = '0.00'
        donors = donations.values('donor').distinct().count()
        context['donors'] = donors
        context['total_amount'] = total_amount
        return context



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
    # if event.due_date & event.due_date >= timezone.now().date():
    #     event.is_completed = True
    #     event.save()
    context = {'event':event}
    return render(request, 'donateApp/donate.html', context)


def donateSave(request, slug):
    event = Event.objects.get(slug=slug)
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        amount = request.POST.get('amount')
        donor = Donor.objects.create(name=name, phone_num=phone)
        Donation.objects.create(
            event=event, 
            donor=donor, 
            amount=amount
        )
        msg = event.thank_you_msg
        send_sms(phone, f'Hello {name},\n{msg}')
        return redirect('donate', slug=event.slug)
    return redirect('donate', slug=event.slug)


@login_required
def createEvent(request):
    form = CreateEventForm()
    if request.method == 'POST':
        form = CreateEventForm(request.POST)
        if form.is_valid():
            event = form.save(commit=False)
            event.admin = request.user
            event.save()
            return redirect('events')
    context = {'form': form}
    return render(request, 'donateApp/create_event.html', context)


@login_required
def updateEvent(request, slug):
    event = Event.objects.get(slug=slug)
    form = CreateEventForm(instance=event)
    if request.method == 'POST':
        form = CreateEventForm(request.POST, request.FILES, instance=event)
        if form.is_valid():
            event = form.save(commit=False)
            event.admin = request.user
            event.save()
            return redirect('event-detail', slug=slug)
    context = {'form': form}
    return render(request, 'donateApp/create_event.html', context)


@login_required
def deleteEvent(request, slug):
    event = Event.objects.get(slug=slug)
    if request.method == 'POST':
        event.delete()
        return redirect('events')
    context = {'event':event}
    return render(request, 'donateApp/delete_event.html', context)


@login_required
def eventState(request, slug):
    event = Event.objects.get(slug=slug)
    if request.method == 'POST':
        if event.is_completed == True:
            event.is_completed = False
        else:
            event.is_completed = True
        event.save()
        return redirect('events')
    context = {'event':event}
    return render(request, 'donateApp/event_state.html', context)




