from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin, SummernoteInlineModelAdmin

from .models import Comment, Posting, PointOfInterest


class CommentInline(admin.StackedInline, SummernoteInlineModelAdmin):
    fields = ('content', )
    model = Comment
    extra = 1

    def save_model(self, request, obj, form, change):
        obj.owner = request.user
        obj.save()



class PostingAdmin(SummernoteModelAdmin):
    list_display = ['owner', 'title', 'category']
    inlines = [CommentInline]
    fields = ('title', 'content', 'category')


class POIAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'latitude', 'longitude']


admin.site.register(Posting, PostingAdmin)
admin.site.register(PointOfInterest, POIAdmin)
