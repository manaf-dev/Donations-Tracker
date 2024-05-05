from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Event(models.Model):
    admin = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=255)
    date_created = models.DateTimeField(auto_now_add=True)
    due_date = models.DateTimeField(blank=True, null=True)
    link = models.CharField(max_length=255)
    is_completed = models.BooleanField(default=False)
    # flyer = models.ImageField(upload_to='event_flyers', default='default.png', null=True, blank=True)


    class Meta:
        verbose_name = 'Event'
        verbose_name_plural = 'Events'

    def __str__(self):
        return self.title


class Donor(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    phone_num = models.CharField(max_length=15)

    class Meta:
        verbose_name_plural = 'Donors'
    
    def __str__(self):
        return self.name


class Donation(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='donations')
    donor = models.ForeignKey(Donor, null=True, on_delete=models.SET_NULL)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Donations'
    
    def __str__(self):
        return f'Donations for {self.event.title}'