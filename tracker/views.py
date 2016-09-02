from rest_framework import viewsets, filters
from rest_framework.permissions import IsAuthenticated

from tracker.models import Tracker
from tracker.serializers import TrackerSerializer
from member.models import Elder, CareGiver

from django.db.models import Q
from django.views.generic import View, ListView, DetailView
from datetime import datetime, date, time
from datetime import timedelta
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from base.views import cek_session
from django.shortcuts import render
import requests
import json


class TrackerList(ListView):
    model = Tracker
    template_name = "partner/tracker_list.html"

    def get_queryset(self):
        return Tracker.objects.filter(~Q(condition='tb'))


class PanicList(ListView):
    model = Tracker
    template_name = "partner/tracker_list.html"

    def get_queryset(self):
        return Tracker.objects.filter(condition='tb')


class Trackers(viewsets.ModelViewSet):

    serializer_class = TrackerSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = ('elder',)

    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        if self.request.user.is_authenticated():
            if CareGiver.objects.filter(user=self.request.user):
                caregiver = CareGiver.objects.get(user=self.request.user)
                return Tracker.objects.filter(
                        elder__in=Elder.get_cared_elder(caregiver))
            elif Elder.objects.filter(user=self.request.user):
                elder = Elder.objects.get(user=self.request.user)
                return Tracker.objects.filter(elder=elder)
        return Tracker.objects.all()
    
    def perform_create(self, serializer):
        tracker = serializer.save()
        elder = tracker.elder
        header = {"Content-Type": "application/json",
            "Authorization": "Basic Njg5MjcxYzgtMDIyOC00MjY1LWE1ZmEtZWMxM2UxMjhjNjAx"}

        payload = {
            "app_id": "a9b5cfe4-e554-40ab-a804-ee63364a96c9",
            "contents": {"en": elder.user.first_name+" "+elder.user.last_name+" mengirimkan kondisi "+tracker.get_condition_display()},
            "headings": {"en": "Update kondisi "+elder.user.first_name+" "+elder.user.last_name},
            "tags": [{"key":elder.id,"relation":"=","value":"true"}],
            "data":{"track":serializer.data}
        }

        if tracker.condition == 'tb':
            payload["headings"] = {"en": "Panggilan panik: "+elder.user.first_name+" "+elder.user.last_name}
            payload["contents"] = {"en": elder.user.first_name+" "+elder.user.last_name+" mengirimkan panggilan panik. Harap segera dihubungi."}

        req = requests.post("https://onesignal.com/api/v1/notifications", headers=header, data=json.dumps(payload))
        print (req.text)


class KondisiHarian(View):
    @classmethod
    def as_view(cls, **initkwargs):
        view = super(KondisiHarian, cls).as_view(**initkwargs)
        return login_required(view, redirect_field_name=None)

    def get(self, request):
        cek_session(request)
        elders = Elder.get_cared_elder(
                    user=CareGiver.objects.get(user=request.user))
        if request.session.get('active_elder') is not None and \
           request.session['active_elder'] != 0:
            elder = Elder.objects.get(pk=request.session.get('active_elder'))
            today = datetime.combine(date.today(), time.min)
            lastweek = today-timedelta(days=7)
            tracker = elder.tracker_set.filter(type="cd")
            graph = tracker.filter(created__gte=lastweek)
            tracker = tracker.order_by('-created')
            return render(request, 'riwayat_kesehatan.html',
                          {'elders': elders, 'active_elder': elder,
                           'tracker': tracker, 'graph': graph,
                           'judul': 'Kondisi Harian'})
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
        elders = Elder.get_cared_elder(
                    user=CareGiver.objects.get(user=request.user))
        if request.session.get('active_elder') is not None and \
           request.session['active_elder'] != 0:
            elder = Elder.objects.get(pk=request.session.get('active_elder'))
            today = datetime.combine(date.today(), time.min)
            lastweek = today-timedelta(days=7)
            tracker = elder.tracker_set.filter(type="hr")
            graph = tracker.filter(created__gte=lastweek)
            tracker = tracker.order_by('-created')
            return render(request, 'riwayat_kesehatan.html',
                          {'elders': elders, 'active_elder': elder,
                           'tracker': tracker, 'graph': graph,
                           'judul': 'Kondisi Harian'})
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
        elders = Elder.get_cared_elder(
                    user=CareGiver.objects.get(user=request.user))
        if request.session.get('active_elder') is not None and \
           request.session['active_elder'] != 0:
            elder = Elder.objects.get(pk=request.session.get('active_elder'))
            today = datetime.combine(date.today(), time.min)
            lastweek = today-timedelta(days=7)
            tracker = elder.tracker_set.filter(type="bg")
            graph = tracker.filter(created__gte=lastweek)
            tracker = tracker.order_by('-created')
            return render(request, 'riwayat_kesehatan.html',
                          {'elders': elders, 'active_elder': elder,
                           'tracker': tracker, 'graph': graph,
                           'judul': 'Gula Darah'})
        return HttpResponseRedirect(reverse('index'))

    def post(self, request):
        return self.get(request, id)
