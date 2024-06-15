from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
from PIL import Image

# Create your models here.
class Event(models.Model):
    admin = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=255)
    date_created = models.DateTimeField(auto_now_add=True)
    due_date = models.DateTimeField(blank=True, null=True)
    is_completed = models.BooleanField(default=False)
    flyer = models.ImageField(upload_to='events_flyers', default='default.png')
    slug = models.SlugField(null=False, unique=True, default="")
    thank_you_msg = models.TextField(blank=True, default='We appreciate your kindness.')
    
    def save(self, *args, **kwargs):
        #create slug
        self.slug = slugify(self.title)
        super(Event, self).save(*args, **kwargs)
        
        #resize flyer
        img = Image.open(self.flyer.path)
        if img.height > 300 or img.width > 300:
            size = (300, 300)
            img.thumbnail(size)
            img.save(self.flyer.path)


    class Meta:
        verbose_name = 'Event'
        verbose_name_plural = 'Events'
        ordering = ['is_completed', '-date_created']

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


    