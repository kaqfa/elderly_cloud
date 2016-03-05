from rest_framework import viewsets, filters

from tracker.models import Tracker
from tracker.serializers import TrackerSerializer
from member.models import Elder, CareGiver

from django.views.generic import View
from datetime import datetime, date, time
from datetime import timedelta
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from base.views import cek_session
from django.shortcuts import render


# Create your views here.

class Trackers(viewsets.ModelViewSet):

    serializer_class = TrackerSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = ('elder',)

    def get_queryset(self):
        if self.request.user.is_authenticated():
            if CareGiver.objects.filter(user=self.request.user):
                caregiver = CareGiver.objects.get(user=self.request.user)
                return Tracker.objects.filter(elder__in=Elder.get_cared_elder(caregiver))
            elif Elder.objects.filter(user=self.request.user):
                elder = Elder.objects.get(user=self.request.user)
                return Tracker.objects.filter(elder=elder)
        return Tracker.objects.all()

class KondisiHarian(View):
    @classmethod
    def as_view(cls, **initkwargs):
        view = super(KondisiHarian, cls).as_view(**initkwargs)
        return login_required(view, redirect_field_name=None)

    def get(self, request):
        cek_session(request)
        elders=Elder.get_cared_elder(user=CareGiver.objects.get(user=request.user))
        if request.session.get('active_elder') is not None and request.session['active_elder']!=0:
            elder=Elder.objects.get(pk=request.session.get('active_elder'))
            today=datetime.combine(date.today(), time.min)
            lastweek=today-timedelta(days=7)
            tracker=elder.tracker_set.filter(type="cd")
            graph=tracker.filter(created__gte=lastweek)
            tracker=tracker.order_by('-created')
            return render(request, 'riwayat_kesehatan.html', {'elders':elders, 'active_elder':elder, 'tracker':tracker, 'graph':graph, 'judul':'Kondisi Harian'})
        return HttpResponseRedirect(reverse('index'))
    def post(self, request):
        return self.get(request, id)

class DetakJantung(View):
    @classmethod
    def as_view(cls, **initkwargs):
        view = super(DetakJantung, cls).as_view(**initkwargs)
        return login_required(view, redirect_field_name=None)

    def get(self, request):
        cek_session(request)
        elders=Elder.get_cared_elder(user=CareGiver.objects.get(user=request.user))
        if request.session.get('active_elder') is not None and request.session['active_elder']!=0:
            elder=Elder.objects.get(pk=request.session.get('active_elder'))
            today=datetime.combine(date.today(), time.min)
            lastweek=today-timedelta(days=7)
            tracker=elder.tracker_set.filter(type="hr")
            graph=tracker.filter(created__gte=lastweek)
            tracker=tracker.order_by('-created')
            return render(request, 'riwayat_kesehatan.html', {'elders':elders, 'active_elder':elder, 'tracker':tracker, 'graph':graph, 'judul':'Kondisi Harian'})
        return HttpResponseRedirect(reverse('index'))
    def post(self, request):
        return self.get(request, id)

class GulaDarah(View):
    @classmethod
    def as_view(cls, **initkwargs):
        view = super(GulaDarah, cls).as_view(**initkwargs)
        return login_required(view, redirect_field_name=None)

    def get(self, request):
        cek_session(request)
        elders=Elder.get_cared_elder(user=CareGiver.objects.get(user=request.user))
        if request.session.get('active_elder') is not None and request.session['active_elder']!=0:
            elder=Elder.objects.get(pk=request.session.get('active_elder'))
            today=datetime.combine(date.today(), time.min)
            lastweek=today-timedelta(days=7)
            tracker=elder.tracker_set.filter(type="bg")
            graph=tracker.filter(created__gte=lastweek)
            tracker=tracker.order_by('-created')
            return render(request, 'riwayat_kesehatan.html', {'elders':elders, 'active_elder':elder, 'tracker':tracker, 'graph':graph, 'judul':'Gula Darah'})
        return HttpResponseRedirect(reverse('index'))
    def post(self, request):
        return self.get(request, id)
