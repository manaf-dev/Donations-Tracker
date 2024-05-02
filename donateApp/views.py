from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def home(request):
    return render(request, 'donateApp/index.html')


def events(request):
    return render(request, 'donateApp/event_list.html')


def event_detail(request):
    return render(request, 'donateApp/event_detail.html')


def donate(request):
    return render(request, 'donateApp/donate.html')


def amount(request):
    return render(request, 'donateApp/amount.html')