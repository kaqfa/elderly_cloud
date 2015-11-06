from rest_framework import viewsets, filters
from notification.models import NotificationTemplate
from notification.serializers import NotificationTemplateSerializer
from member.models import Elder, CareGiver
from django.db.models import Q
from django.views.generic import View
from base.views import cek_session
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import HttpResponseRedirect
from datetime import datetime

from notification.models import Notification
from notification.serializers import NotificationSerializer
from notification.forms import NotificationForm
from django.core.urlresolvers import reverse
from django.contrib import messages
from itertools import chain


# Create your views here.

class Notifs(viewsets.ModelViewSet):
    serializer_class = NotificationSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = ('receiver',)

    def get_queryset(self):
        user = self.request.user
        if user.is_authenticated():
            if CareGiver.objects.filter(user=user):
                caregiver = CareGiver.objects.get(user=user)
                elder = Elder.get_cared_elder(caregiver).values_list('user', flat=True).order_by('id')
                return Notification.objects.filter(Q(sender=user) | Q(receiver=user) | Q(receiver__in=elder))
            elif Elder.objects.filter(user=user):
                elder = Elder.objects.get(user=user)
                caregiver = CareGiver.objects.filter(elder__in=[elder]).values_list('user', flat=True).order_by('id')
                return Notification.objects.filter(Q(sender=user) | Q(receiver=user) | Q(receiver__in=caregiver))
        return Notification.objects.all()


class Hello(viewsets.ReadOnlyModelViewSet):
    serializer_class = NotificationTemplateSerializer

    def get_queryset(self):
        return NotificationTemplate.objects.all()

class NotifikasiElder(View):
    @classmethod
    def as_view(cls, **initkwargs):
        view = super(NotifikasiElder, cls).as_view(**initkwargs)
        return login_required(view, redirect_field_name=None)

    def get(self, request):
        cek_session(request)
        elder=None
        if request.session.get('active_elder') is not None and request.session['active_elder']!=0:
            elder=Elder.objects.get(pk=request.session.get('active_elder'))
            elders=Elder.get_cared_elder(user=CareGiver.objects.get(user=request.user))
            notif=Notification.objects.filter(receiver=elder.user)
            return render(request, 'notif.html', {'elders':elders, 'active_elder':elder, 'notifs':notif, 'untuk':1})
        else:
            return HttpResponseRedirect(reverse('index'))
    def post(self, request):
        cek_session(request)
        elder=None
        if request.session.get('active_elder') is not None and request.session['active_elder']!=0:
            elder=Elder.objects.get(pk=request.session.get('active_elder'))
            elders=Elder.get_cared_elder(user=CareGiver.objects.get(user=request.user))
            form = NotificationForm(request.POST)
            notif=Notification.objects.filter(receiver=elder.user)
            if form.is_valid():
                new=form.save(commit=False)
                new.sender=request.user
                new.receiver=elder.user
                new.status='s'
                new.save()
                notif=Notification.objects.filter(receiver=elder.user)
                return render(request, 'notif.html', {'elders':elders, 'success':"Notifikasi berhasil ditambahkan", 'active_elder':elder, 'notifs':notif, 'untuk':"Orang Tua"})
            else:
                return render(request, 'notif.html', {'elders':elders, 'error':form.errors, 'active_elder':elder, 'notifs':notif, 'untuk':"Orang Tua"})
        else:
            return HttpResponseRedirect(reverse('index'))

class DetailNotifikasiElder(View):
    @classmethod
    def as_view(cls, **initkwargs):
        view = super(DetailNotifikasiElder, cls).as_view(**initkwargs)
        return login_required(view, redirect_field_name=None)

    def get(self, request, id):
        cek_session(request)
        if request.session.get('active_elder') is not None and request.session['active_elder']!=0:
            elder=Elder.objects.get(pk=request.session.get('active_elder'))
            elders=Elder.get_cared_elder(user=CareGiver.objects.get(user=request.user))
            notif=Notification.objects.filter(receiver=elder.user, id=id)
            if notif:
                return render(request, 'notif_read.html', {'elders':elders, 'active_elder':elder, 'notif':notif[0]})
            return HttpResponseRedirect(reverse('notif_elder'))
        return HttpResponseRedirect(reverse('index'))
    def post(self, request, id):
        return self.get(request, id)

class EditNotifikasiElder(View):
    @classmethod
    def as_view(cls, **initkwargs):
        view = super(EditNotifikasiElder, cls).as_view(**initkwargs)
        return login_required(view, redirect_field_name=None)

    def get(self, request, id):
        cek_session(request)
        if request.session.get('active_elder') is not None and request.session['active_elder']!=0:
            elder=Elder.objects.get(pk=request.session.get('active_elder'))
            elders=Elder.get_cared_elder(user=CareGiver.objects.get(user=request.user))
            notif=Notification.objects.filter(receiver=elder.user, id=id)
            if notif:
                return render(request, 'notif_edit.html', {'elders':elders, 'active_elder':elder, 'notif':notif[0]})
            return HttpResponseRedirect(reverse('notif_elder'))
        return HttpResponseRedirect(reverse('index'))
    def post(self, request, id):
        cek_session(request)
        if request.session.get('active_elder') is not None and request.session['active_elder']!=0:
            elder=Elder.objects.get(pk=request.session.get('active_elder'))
            elders=Elder.get_cared_elder(user=CareGiver.objects.get(user=request.user))
            notif=Notification.objects.filter(receiver=elder.user, id=id)
            if notif:
                form = NotificationForm(request.POST, instance=notif[0])
                if form.is_valid():
                    notif=form.save()
                    return render(request, 'notif_edit.html', {'elders':elders, 'success':"Notifikasi berhasil dirubah", 'active_elder':elder, 'notif':notif})
                return render(request, 'notif_edit.html', {'elders':elders, 'active_elder':elder, 'error':form.errors, 'notif':notif[0]})
            return HttpResponseRedirect(reverse('notif_elder'))
        return HttpResponseRedirect(reverse('index'))
        
class HapusNotifikasiElder(View):
    @classmethod
    def as_view(cls, **initkwargs):
        view = super(HapusNotifikasiElder, cls).as_view(**initkwargs)
        return login_required(view, redirect_field_name=None)

    def get(self, request, id):
        cek_session(request)
        if request.session.get('active_elder') is not None and request.session['active_elder']!=0:
            elder=Elder.objects.get(pk=request.session.get('active_elder'))
            elders=Elder.get_cared_elder(user=CareGiver.objects.get(user=request.user))
            notif=Notification.objects.filter(receiver=elder.user, id=id)
            if notif:
                return render(request, 'notif_delete.html', {'elders':elders, 'active_elder':elder, 'notif':notif[0]})
            return HttpResponseRedirect(reverse('notif_elder'))
        return HttpResponseRedirect(reverse('index'))
    def post(self, request, id):
        cek_session(request)
        if request.session.get('active_elder') is not None and request.session['active_elder']!=0:
            elder=Elder.objects.get(pk=request.session.get('active_elder'))
            elders=Elder.get_cared_elder(user=CareGiver.objects.get(user=request.user))
            notif=Notification.objects.filter(receiver=elder.user, id=id)
            if notif:
                name=notif[0].title
                notif.delete()
                messages.success(request, 'Notifikasi "'+name+'" telah berhasil dihapus.')
        return HttpResponseRedirect(reverse('notif_elder'))
        
class NotifikasiCG(View):
    @classmethod
    def as_view(cls, **initkwargs):
        view = super(NotifikasiCG, cls).as_view(**initkwargs)
        return login_required(view, redirect_field_name=None)

    def get(self, request):
        cek_session(request)
        elder=None
        notif1=request.user.get_unread_notif()
        elders=Elder.get_cared_elder(user=CareGiver.objects.get(user=request.user))
        if request.session.get('active_elder') is not None and request.session['active_elder']!=0:
            elder=Elder.objects.get(pk=request.session.get('active_elder'))
            notif2=Notification.objects.filter(receiver=elder.user, status='s', invoked_on__lte=datetime.now()).order_by('invoked_on')
            notif=list(chain(notif1, notif2))
        notif3=request.user.notif_receiver.filter(status='r').order_by('-invoked_on', '-modified')
        notif=list(chain(notif, notif3))
        return render(request, 'notif.html', {'elders':elders, 'active_elder':elder, 'notifs':notif, 'untuk':2})
        
class DetailNotifikasiCG(View):
    @classmethod
    def as_view(cls, **initkwargs):
        view = super(DetailNotifikasiCG, cls).as_view(**initkwargs)
        return login_required(view, redirect_field_name=None)

    def get(self, request, id):
        cek_session(request)
        elders=Elder.get_cared_elder(user=CareGiver.objects.get(user=request.user))
        if request.session.get('active_elder') is not None and request.session['active_elder']!=0:
            elder=Elder.objects.get(pk=request.session.get('active_elder'))
        notif=Notification.objects.filter(receiver=request.user, id=id)
        if notif:
            return render(request, 'notif_read.html', {'elders':elders, 'active_elder':elder, 'notif':notif[0]})
        return HttpResponseRedirect(reverse('notif_cg'))
    def post(self, request, id):
        return self.get(request, id)
        
class ResponNotifikasi(View):
    @classmethod
    def as_view(cls, **initkwargs):
        view = super(ResponNotifikasi, cls).as_view(**initkwargs)
        return login_required(view, redirect_field_name=None)

    def get(self, request, id):
        cek_session(request)
        elders=Elder.get_cared_elder(user=CareGiver.objects.get(user=request.user))
        if request.session.get('active_elder') is not None and request.session['active_elder']!=0:
            elder=Elder.objects.get(pk=request.session.get('active_elder'))
        notif=Notification.objects.filter(receiver=request.user, id=id)
        if notif:
            return render(request, 'notif_response.html', {'elders':elders, 'active_elder':elder, 'notif':notif[0]})
        return HttpResponseRedirect(reverse('notif_cg'))
    def post(self, request, id):
        cek_session(request)
        elders=Elder.get_cared_elder(user=CareGiver.objects.get(user=request.user))
        if request.session.get('active_elder') is not None and request.session['active_elder']!=0:
            elder=Elder.objects.get(pk=request.session.get('active_elder'))
        notif=Notification.objects.filter(receiver=request.user, id=id)
        if notif:
            notif=notif[0]
            notif.status='r'
            notif.save()
            messages.success(request, 'Notifikasi "'+notif.title+'" telah berhasil direspon.')
        return HttpResponseRedirect(reverse('notif_cg'))