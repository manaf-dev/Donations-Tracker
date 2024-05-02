from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def home(request):
    return render(request, 'donateApp/index.html')


def events(request):
    return render(request, 'donateApp/events.html')