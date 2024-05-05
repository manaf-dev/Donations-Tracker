from django import forms
from .models import Event



class CreateEventForm(forms.ModelForm):
    
    class Meta:
        model = Event
        fields = ("title", "description", "due_date")


