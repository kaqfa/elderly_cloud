from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin

from .models import Notification, NotificationTemplate


class NotifTemplateAdmin(SummernoteModelAdmin):
    list_display = ['title', 'content', 'level']


class NotificationAdmin(SummernoteModelAdmin):
    list_display = ['title', 'content', 'invoked_on',
                    'recurring', 'sender', 'receiver', 'status']


admin.site.register(Notification, NotificationAdmin)
admin.site.register(NotificationTemplate, NotifTemplateAdmin)