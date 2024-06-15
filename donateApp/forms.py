from django import forms
from .models import Event



class CreateEventForm(forms.ModelForm):
    
    class Meta:
        model = Event
        fields = ("title", "description", "thank_you_msg", "due_date", "flyer")
        help_texts = {
            'due_date': 'Due date (if any)',
            'flyer': 'Upload event flyer.',
        }

        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Enter event title'}),
            'description': forms.Textarea(attrs={'placeholder': 'Describe your event'}),
            'thank_you_msg': forms.Textarea(attrs={'placeholder':'Thank you message for your donors.', 'default':''}),
            'due_date': forms.TextInput(attrs={'type':'date'})

        }



