from django.contrib import admin

from .models import Elder, CareGiver, Partner


class CaregiverAdmin(admin.ModelAdmin):
    list_display = ['user', 'address', 'birthday', 'phone']


class ElderAdmin(admin.ModelAdmin):
    list_display = ['user', 'code', 'address', 'birthday', 'phone']


class PartnerAdmin(admin.ModelAdmin):
    list_display = ['user', 'address', 'phone', 'type']


admin.site.register(CareGiver, CaregiverAdmin)
admin.site.register(Elder, ElderAdmin)
admin.site.register(Partner, PartnerAdmin)