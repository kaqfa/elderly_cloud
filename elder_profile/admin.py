from django.contrib import admin
from .models import DiseaseHist, MedicalTreatmentHist, Note


class DiseaseAdmin(admin.ModelAdmin):
    list_display = ['elder', 'name', 'from_year', 'to_year', 'status']


class TreatmentAdmin(admin.ModelAdmin):
    list_display = ['elder', 'treatment', 'from_year', 'to_year', 'status']


class NoteAdmin(admin.ModelAdmin):
    list_display = ['user', 'elder', 'title', 'sharable']


admin.site.register(DiseaseHist, DiseaseAdmin)
admin.site.register(MedicalTreatmentHist, TreatmentAdmin)
admin.site.register(Note, NoteAdmin)