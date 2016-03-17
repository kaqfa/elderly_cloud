from django.contrib import admin

from .models import Tracker


class TrackerAdmin(admin.ModelAdmin):
    fields = ['elder', 'type', 'condition', 'location']
    list_display = ['elder', 'condition', 'type', 'value']


admin.site.register(Tracker, TrackerAdmin)
