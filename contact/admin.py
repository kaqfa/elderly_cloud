from django.contrib import admin

from .models import Contact


class ContactAdmin(admin.ModelAdmin):
    list_display = ['elder', 'added_by', 'name', 'email', 'phone']
    fieldsets = (
        ("Form Kontak",
         {
             'classes': ('wide',),
             'fields': ('elder', 'name', 'address', 'phone', 'email', 'status')}),
    )

    def save_model(self, request, obj, form, change):
        obj.added_by = request.user
        obj.save()


admin.site.register(Contact, ContactAdmin)