from rest_framework import viewsets, filters

from elder_profile.models import DiseaseHist, MedicalTreatmentHist
from elder_profile.serializers import DiseaseHistSerializer, MedicalTreatmentHistSerializer
from elder_profile.forms import MedicalTreatmentForm, DiseaseHistForm
from member.models import Elder, CareGiver

from django.views.generic import View
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from base.views import cek_session
from django.shortcuts import render
from django.contrib import messages


# Create your views here.

class Diseases(viewsets.ModelViewSet):
    serializer_class = DiseaseHistSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = ('elder',)

    def get_queryset(self):
        if self.request.user.is_authenticated():
            if CareGiver.objects.filter(user=self.request.user):
                caregiver = CareGiver.objects.get(user=self.request.user)
                return DiseaseHist.objects.filter(elder__in=Elder.get_cared_elder(caregiver))
            elif Elder.objects.filter(user=self.request.user):
                elder = Elder.objects.get(user=self.request.user)
                return DiseaseHist.objects.filter(elder=elder)
        return DiseaseHist.objects.all()


class MedicalTreatments(viewsets.ModelViewSet):
    serializer_class = MedicalTreatmentHistSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = ('elder',)

    def get_queryset(self):
        if self.request.user.is_authenticated():
            if CareGiver.objects.filter(user=self.request.user):
                caregiver = CareGiver.objects.get(user=self.request.user)
                return MedicalTreatmentHist.objects.filter(elder__in=Elder.get_cared_elder(caregiver))
            elif Elder.objects.filter(user=self.request.user):
                elder = Elder.objects.get(user=self.request.user)
                return MedicalTreatmentHist.objects.filter(elder=elder)
        return MedicalTreatmentHist.objects.all()

class MTTable(View):
    @classmethod
    def as_view(cls, **initkwargs):
        view = super(MTTable, cls).as_view(**initkwargs)
        return login_required(view, redirect_field_name=None)

    def get(self, request):
        cek_session(request)
        elder=None
        if request.session.get('active_elder') is not None and request.session['active_elder']!=0:
            elder=Elder.objects.get(pk=request.session.get('active_elder'))
            elders=Elder.get_cared_elder(user=CareGiver.objects.get(user=request.user))
            medis=MedicalTreatmentHist.objects.filter(elder=elder)
            return render(request, 'medis.html', {'elders':elders, 'active_elder':elder, 'medis':medis})
        else:
            return HttpResponseRedirect(reverse('index'))
    def post(self, request):
        cek_session(request)
        elder=None
        if request.session.get('active_elder') is not None and request.session['active_elder']!=0:
            elder=Elder.objects.get(pk=request.session.get('active_elder'))
            elders=Elder.get_cared_elder(user=CareGiver.objects.get(user=request.user))
            form = MedicalTreatmentForm(request.POST)
            medis=MedicalTreatmentHist.objects.filter(elder=elder)
            if form.is_valid():
                new=form.save(commit=False)
                new.elder=elder
                new.save()
                medis=MedicalTreatmentHist.objects.filter(elder=elder)
                return render(request, 'medis.html', {'elders':elders, 'success':"Data berhasil ditambahkan", 'active_elder':elder, 'medis':medis})
            else:
                return render(request, 'medis.html', {'elders':elders, 'error':form.errors, 'active_elder':elder, 'medis':medis})
        else:
            return HttpResponseRedirect(reverse('index'))
            
class MTDetail(View):
    @classmethod
    def as_view(cls, **initkwargs):
        view = super(MTDetail, cls).as_view(**initkwargs)
        return login_required(view, redirect_field_name=None)

    def get(self, request, id):
        cek_session(request)
        if request.session.get('active_elder') is not None and request.session['active_elder']!=0:
            elder=Elder.objects.get(pk=request.session.get('active_elder'))
            elders=Elder.get_cared_elder(user=CareGiver.objects.get(user=request.user))
            medis=MedicalTreatmentHist.objects.filter(elder=elder, id=id)
            if medis:
                return render(request, 'medis_read.html', {'elders':elders, 'active_elder':elder, 'medis':medis[0]})
            return HttpResponseRedirect(reverse('treatment'))
        return HttpResponseRedirect(reverse('index'))
    def post(self, request, id):
        return self.get(request, id)
        
class MTEdit(View):
    @classmethod
    def as_view(cls, **initkwargs):
        view = super(MTEdit, cls).as_view(**initkwargs)
        return login_required(view, redirect_field_name=None)

    def get(self, request, id):
        cek_session(request)
        if request.session.get('active_elder') is not None and request.session['active_elder']!=0:
            elder=Elder.objects.get(pk=request.session.get('active_elder'))
            elders=Elder.get_cared_elder(user=CareGiver.objects.get(user=request.user))
            medis=MedicalTreatmentHist.objects.filter(elder=elder, id=id)
            if medis:
                return render(request, 'medis_edit.html', {'elders':elders, 'active_elder':elder, 'medis':medis[0]})
            return HttpResponseRedirect(reverse('treatment'))
        return HttpResponseRedirect(reverse('index'))
    def post(self, request, id):
        cek_session(request)
        if request.session.get('active_elder') is not None and request.session['active_elder']!=0:
            elder=Elder.objects.get(pk=request.session.get('active_elder'))
            elders=Elder.get_cared_elder(user=CareGiver.objects.get(user=request.user))
            medis=MedicalTreatmentHist.objects.filter(elder=elder, id=id)
            if medis:
                form = MedicalTreatmentForm(request.POST, instance=medis[0])
                if form.is_valid():
                    medis=form.save()
                    return render(request, 'medis_edit.html', {'elders':elders, 'success':"Data berhasil dirubah", 'active_elder':elder, 'medis':medis})
                return render(request, 'medis_edit.html', {'elders':elders, 'active_elder':elder, 'error':form.errors, 'medis':medis[0]})
            return HttpResponseRedirect(reverse('treatment'))
        return HttpResponseRedirect(reverse('index'))
        
class MTDelete(View):
    @classmethod
    def as_view(cls, **initkwargs):
        view = super(MTDelete, cls).as_view(**initkwargs)
        return login_required(view, redirect_field_name=None)

    def get(self, request, id):
        cek_session(request)
        if request.session.get('active_elder') is not None and request.session['active_elder']!=0:
            elder=Elder.objects.get(pk=request.session.get('active_elder'))
            elders=Elder.get_cared_elder(user=CareGiver.objects.get(user=request.user))
            medis=MedicalTreatmentHist.objects.filter(elder=elder, id=id)
            if medis:
                return render(request, 'medis_delete.html', {'elders':elders, 'active_elder':elder, 'medis':medis[0]})
            return HttpResponseRedirect(reverse('treatment'))
        return HttpResponseRedirect(reverse('index'))
    def post(self, request, id):
        cek_session(request)
        if request.session.get('active_elder') is not None and request.session['active_elder']!=0:
            elder=Elder.objects.get(pk=request.session.get('active_elder'))
            elders=Elder.get_cared_elder(user=CareGiver.objects.get(user=request.user))
            medis=MedicalTreatmentHist.objects.filter(elder=elder, id=id)
            if medis:
                name=medis[0].treatment
                medis.delete()
                messages.success(request, 'Data "'+name+'" telah berhasil dihapus.')
        return HttpResponseRedirect(reverse('treatment'))
        
class DHTable(View):
    @classmethod
    def as_view(cls, **initkwargs):
        view = super(DHTable, cls).as_view(**initkwargs)
        return login_required(view, redirect_field_name=None)

    def get(self, request):
        cek_session(request)
        elder=None
        if request.session.get('active_elder') is not None and request.session['active_elder']!=0:
            elder=Elder.objects.get(pk=request.session.get('active_elder'))
            elders=Elder.get_cared_elder(user=CareGiver.objects.get(user=request.user))
            disease=DiseaseHist.objects.filter(elder=elder)
            return render(request, 'disease.html', {'elders':elders, 'active_elder':elder, 'disease':disease})
        else:
            return HttpResponseRedirect(reverse('index'))
    def post(self, request):
        cek_session(request)
        elder=None
        if request.session.get('active_elder') is not None and request.session['active_elder']!=0:
            elder=Elder.objects.get(pk=request.session.get('active_elder'))
            elders=Elder.get_cared_elder(user=CareGiver.objects.get(user=request.user))
            form = DiseaseHistForm(request.POST)
            disease=DiseaseHist.objects.filter(elder=elder)
            if form.is_valid():
                new=form.save(commit=False)
                new.elder=elder
                new.save()
                disease=DiseaseHist.objects.filter(elder=elder)
                return render(request, 'disease.html', {'elders':elders, 'success':"Data berhasil ditambahkan", 'active_elder':elder, 'disease':disease})
            else:
                return render(request, 'disease.html', {'elders':elders, 'error':form.errors, 'active_elder':elder, 'disease':disease})
        else:
            return HttpResponseRedirect(reverse('index'))
            
class DHDetail(View):
    @classmethod
    def as_view(cls, **initkwargs):
        view = super(DHDetail, cls).as_view(**initkwargs)
        return login_required(view, redirect_field_name=None)

    def get(self, request, id):
        cek_session(request)
        if request.session.get('active_elder') is not None and request.session['active_elder']!=0:
            elder=Elder.objects.get(pk=request.session.get('active_elder'))
            elders=Elder.get_cared_elder(user=CareGiver.objects.get(user=request.user))
            disease=DiseaseHist.objects.filter(elder=elder, id=id)
            if disease:
                return render(request, 'disease_read.html', {'elders':elders, 'active_elder':elder, 'disease':disease[0]})
            return HttpResponseRedirect(reverse('treatment'))
        return HttpResponseRedirect(reverse('index'))
    def post(self, request, id):
        return self.get(request, id)
        
class DHEdit(View):
    @classmethod
    def as_view(cls, **initkwargs):
        view = super(DHEdit, cls).as_view(**initkwargs)
        return login_required(view, redirect_field_name=None)

    def get(self, request, id):
        cek_session(request)
        if request.session.get('active_elder') is not None and request.session['active_elder']!=0:
            elder=Elder.objects.get(pk=request.session.get('active_elder'))
            elders=Elder.get_cared_elder(user=CareGiver.objects.get(user=request.user))
            disease=DiseaseHist.objects.filter(elder=elder, id=id)
            if disease:
                return render(request, 'disease_edit.html', {'elders':elders, 'active_elder':elder, 'disease':disease[0]})
            return HttpResponseRedirect(reverse('treatment'))
        return HttpResponseRedirect(reverse('index'))
    def post(self, request, id):
        cek_session(request)
        if request.session.get('active_elder') is not None and request.session['active_elder']!=0:
            elder=Elder.objects.get(pk=request.session.get('active_elder'))
            elders=Elder.get_cared_elder(user=CareGiver.objects.get(user=request.user))
            disease=DiseaseHist.objects.filter(elder=elder, id=id)
            if disease:
                form = DiseaseHistForm(request.POST, instance=disease[0])
                if form.is_valid():
                    disease=form.save()
                    return render(request, 'disease_edit.html', {'elders':elders, 'success':"Data berhasil dirubah", 'active_elder':elder, 'disease':disease})
                return render(request, 'disease_edit.html', {'elders':elders, 'active_elder':elder, 'error':form.errors, 'disease':disease[0]})
            return HttpResponseRedirect(reverse('treatment'))
        return HttpResponseRedirect(reverse('index'))
        
class DHDelete(View):
    @classmethod
    def as_view(cls, **initkwargs):
        view = super(DHDelete, cls).as_view(**initkwargs)
        return login_required(view, redirect_field_name=None)

    def get(self, request, id):
        cek_session(request)
        if request.session.get('active_elder') is not None and request.session['active_elder']!=0:
            elder=Elder.objects.get(pk=request.session.get('active_elder'))
            elders=Elder.get_cared_elder(user=CareGiver.objects.get(user=request.user))
            disease=DiseaseHist.objects.filter(elder=elder, id=id)
            if disease:
                return render(request, 'disease_delete.html', {'elders':elders, 'active_elder':elder, 'disease':disease[0]})
            return HttpResponseRedirect(reverse('treatment'))
        return HttpResponseRedirect(reverse('index'))
    def post(self, request, id):
        cek_session(request)
        if request.session.get('active_elder') is not None and request.session['active_elder']!=0:
            elder=Elder.objects.get(pk=request.session.get('active_elder'))
            elders=Elder.get_cared_elder(user=CareGiver.objects.get(user=request.user))
            disease=DiseaseHist.objects.filter(elder=elder, id=id)
            if disease:
                name=disease[0].name
                disease.delete()
                messages.success(request, 'Data "'+name+'" telah berhasil dihapus.')
        return HttpResponseRedirect(reverse('treatment'))