from django.contrib import admin

from .models import Elder, CareGiver, Partner, CareGiving, Member


class CaregiverAdmin(admin.ModelAdmin):
    list_display = ['user', 'address', 'birthday', 'phone']


class MemberAdmin(admin.ModelAdmin):
	list_display = ['first_name', 'last_name', 'email']


class ElderAdmin(admin.ModelAdmin):
    list_display = ['user', 'code', 'address', 'birthday', 'phone']


class CareGivingAdmin(admin.ModelAdmin):
    list_display = ['caregiver', 'elder']


class PartnerAdmin(admin.ModelAdmin):
    list_display = ['user', 'address', 'phone', 'type']


admin.site.register(CareGiver, CaregiverAdmin)
admin.site.register(Member, MemberAdmin)
admin.site.register(Elder, ElderAdmin)
admin.site.register(Partner, PartnerAdmin)
admin.site.register(CareGiving, CareGivingAdmin)
