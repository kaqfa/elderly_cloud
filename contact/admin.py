from django.contrib import admin
from .models import Contact


class ContactAdmin(admin.ModelAdmin):
    list_display = ['elder', 'added_by', 'name', 'email', 'phone']


admin.site.register(Contact, ContactAdmin)