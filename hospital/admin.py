from django.contrib import admin
from .models import Hospital

# Register your models here.
class HospitalAdmin(admin.ModelAdmin):
    list_display = ['name', 'address', 'phone']

# Register your models here.
admin.site.register(Hospital, HospitalAdmin)