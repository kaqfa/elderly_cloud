from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin, SummernoteInlineModelAdmin

from .models import Response, Feedback


class ResponeInline(admin.StackedInline, SummernoteInlineModelAdmin):
    model = Response
    extra = 1


class FeedbackAdmin(SummernoteModelAdmin):
    list_display = ['owner', 'title', 'status']
    inlines = [ResponeInline]


admin.site.register(Feedback, FeedbackAdmin)