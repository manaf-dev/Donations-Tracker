from django.contrib import admin

from .models import Event
from .models import Donor
from .models import Donation


# Register your models here.
admin.site.register(Event)
admin.site.register(Donor)
admin.site.register(Donation)