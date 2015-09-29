from django.contrib import admin
from .models import Response, Feedback
from django_summernote.admin import SummernoteModelAdmin, SummernoteInlineModelAdmin


class ResponeInline(admin.StackedInline, SummernoteInlineModelAdmin):
    model = Response
    extra = 1


class FeedbackAdmin(SummernoteModelAdmin):
    list_display = ['owner', 'title', 'status']
    inlines = [ResponeInline]


admin.site.register(Feedback, FeedbackAdmin)