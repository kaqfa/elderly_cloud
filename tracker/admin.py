from django.contrib import admin

from .models import Tracker, TrackCondition, TrackPanic


class TrackerAdmin(admin.ModelAdmin):
    fields = ['elder', 'type', 'condition', 'location']
    list_display = ['elder', 'condition', 'type', 'value', 'created']


class ConditionAdmin(admin.ModelAdmin):
	fields = ['elder', 'type', 'condition', 'location']
	list_display = ['elder', 'condition', 'type', 'value']


class PanicAdmin(admin.ModelAdmin):
	fields = ['elder', 'type', 'condition', 'location']
	list_display = ['elder', 'condition', 'type', 'value']


admin.site.register(Tracker, TrackerAdmin)
admin.site.register(TrackCondition, ConditionAdmin)
admin.site.register(TrackPanic, PanicAdmin)