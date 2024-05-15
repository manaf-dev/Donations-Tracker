from django import forms
from .models import Event



class CreateEventForm(forms.ModelForm):
    
    class Meta:
        model = Event
        fields = ("title", "description", "due_date", "flyer")

        widgets = {
            'title': forms.TextInput(attrs={'class':'input','placeholder': 'Enter event title'}),
            'description': forms.Textarea(attrs={'class': 'text-area-input', 'placeholder': 'Describe your event'}),
            'due_date': forms.DateInput(attrs={'class': 'input'}),
            'flyer': forms.FileInput(attrs={'class': 'img-input input'}),
        }



