from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin, SummernoteInlineModelAdmin

from .models import Response, Feedback


class ResponeInline(admin.StackedInline, SummernoteInlineModelAdmin):
    fields = ('content',)
    model = Response
    extra = 1


class FeedbackAdmin(SummernoteModelAdmin):
    list_display = ['owner', 'title', 'status']
    inlines = [ResponeInline]
    fields = ('title', 'content', 'status')

    def has_change_permission(self, request, obj=None):
        return True


admin.site.register(Feedback, FeedbackAdmin)
