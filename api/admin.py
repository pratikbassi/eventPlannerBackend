from django.contrib import admin

# Register your models here.
from .models import Event, Track

admin.site.register(Event)
admin.site.register(Track)