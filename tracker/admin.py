from django.contrib import admin
from .models import Tracker


class TrackerAdmin(admin.ModelAdmin):
    list_display = ['elder', 'condition', 'type', 'value']


admin.site.register(Tracker, TrackerAdmin)