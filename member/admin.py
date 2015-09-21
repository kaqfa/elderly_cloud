from django.contrib import admin
from .models import User, Elder


class CaregiverAdmin(admin.ModelAdmin):
    pass


class ElderAdmin(admin.ModelAdmin):
    pass


#admin.site.register(Caregiving, CaregiverAdmin)
admin.site.register(Elder, ElderAdmin)