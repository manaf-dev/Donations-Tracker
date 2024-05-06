from django.contrib import admin

from .models import Event
from .models import Donor
from .models import Donation


# Register your models here.
class EventAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('title',)}


admin.site.register(Event, EventAdmin)
admin.site.register(Donor)
admin.site.register(Donation)