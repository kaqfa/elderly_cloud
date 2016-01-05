# Create your views here.
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from django.http import HttpResponseRedirect, HttpResponse
from django.views.generic import View
from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from base.views import cek_session, is_caregiver
from partner.forms import AvailabilityForm, AgendaForm, RoomForm, RoomClassForm
from partner.models import Availability, Agenda, Room, RoomClass

class UpdateAvailability(View):
    
    @classmethod
    def as_view(cls, **initkwargs):
        view = super(UpdateAvailability, cls).as_view(**initkwargs)
        return login_required(view, redirect_field_name=None)

    def get(self, request):
        if is_caregiver(request.user):
                return HttpResponseRedirect(reverse('index'))
        else:
            return HttpResponseRedirect(reverse('index'))
    
    def post(self, request):
        if is_caregiver(request.user):
                return HttpResponseRedirect(reverse('index'))
        else:
            availability = Availability.objects.filter(owner=request.user.member)
            if availability:
                form = AvailabilityForm(request.POST,instance=availability[0])
            else:
                form = AvailabilityForm(request.POST)
            if form.is_valid():
                avail=form.save(commit=False)
                avail.owner=request.user.member
                avail.save()
            else:
                for num, errors in form.errors.items():
                    for e in errors:
                        messages.error(request, e)
            return HttpResponseRedirect(reverse("index"))
            
class AgendaTable(View):
    @classmethod
    def as_view(cls, **initkwargs):
        view = super(AgendaTable, cls).as_view(**initkwargs)
        return login_required(view, redirect_field_name=None)

    def get(self, request):
        agenda=Agenda.objects.filter(owner=request.user.member).order_by('-id')
        return render(request, 'agenda.html', {'agenda':agenda})
    def post(self, request):
        form = AgendaForm(request.POST)
        agenda=Agenda.objects.filter(owner=request.user.member).order_by('-id')
        if form.is_valid():
            new=form.save(commit=False)
            new.owner=request.user.member
            new.save()
            agenda=Agenda.objects.filter(owner=request.user.member).order_by('-id')
            return render(request, 'agenda.html', {'success':"Data berhasil ditambahkan", 'agenda':agenda})
        else:
            return render(request, 'agenda.html', {'error':form.errors, 'agenda':agenda})
            
class AgendaDetail(View):
    @classmethod
    def as_view(cls, **initkwargs):
        view = super(AgendaDetail, cls).as_view(**initkwargs)
        return login_required(view, redirect_field_name=None)

    def get(self, request, id):
        agenda=Agenda.objects.filter(owner=request.user.member, id=id)
        if agenda:
            return render(request, 'agenda_read.html', {'agenda':agenda[0]})
        return HttpResponseRedirect(reverse('agenda'))
    def post(self, request, id):
        return self.get(request, id)
        
class AgendaEdit(View):
    @classmethod
    def as_view(cls, **initkwargs):
        view = super(AgendaEdit, cls).as_view(**initkwargs)
        return login_required(view, redirect_field_name=None)

    def get(self, request, id):
            agenda=Agenda.objects.filter(owner=request.user.member, id=id)
            if agenda:
                return render(request, 'agenda_edit.html', {'agenda':agenda[0]})
            return HttpResponseRedirect(reverse('agenda'))
    def post(self, request, id):
        agenda=Agenda.objects.filter(owner=request.user.member, id=id)
        if agenda:
            form = AgendaForm(request.POST, instance=agenda[0])
            if form.is_valid():
                agenda=form.save()
                return render(request, 'agenda_edit.html', {'success':"Data berhasil dirubah", 'agenda':agenda})
            return render(request, 'agenda_edit.html', {'error':form.errors, 'agenda':agenda[0]})
        return HttpResponseRedirect(reverse('agenda'))
        
class AgendaDelete(View):
    @classmethod
    def as_view(cls, **initkwargs):
        view = super(AgendaDelete, cls).as_view(**initkwargs)
        return login_required(view, redirect_field_name=None)

    def get(self, request, id):
        agenda=Agenda.objects.filter(owner=request.user.member, id=id)
        if agenda:
            return render(request, 'agenda_delete.html', {'agenda':agenda[0]})
        return HttpResponseRedirect(reverse('agenda'))
    def post(self, request, id):
        agenda=Agenda.objects.filter(owner=request.user.member, id=id)
        if agenda:
            name=agenda[0].name
            agenda.delete()
            messages.success(request, 'Data "'+name+'" telah berhasil dihapus.')
        return HttpResponseRedirect(reverse('agenda'))
        
class RoomTable(View):
    @classmethod
    def as_view(cls, **initkwargs):
        view = super(RoomTable, cls).as_view(**initkwargs)
        return login_required(view, redirect_field_name=None)

    def get(self, request):
        room=Room.objects.filter(owner=request.user.member).order_by('-id')
        rc=RoomClass.objects.filter(owner=request.user.member).order_by('-id')
        return render(request, 'room.html', {'room':room, 'rc':rc})
    def post(self, request):
        form = RoomForm(request.POST)
        rc=RoomClass.objects.filter(owner=request.user.member).order_by('-id')
        room=Room.objects.filter(owner=request.user.member).order_by('-id')
        if form.is_valid():
            new=form.save(commit=False)
            new.owner=request.user.member
            new.save()
            room=Room.objects.filter(owner=request.user.member).order_by('-id')
            return render(request, 'room.html', {'success':"Data berhasil ditambahkan", 'room':room, 'rc':rc})
        else:
            return render(request, 'room.html', {'error':form.errors, 'room':room, 'rc':rc})
            
class RoomDetail(View):
    @classmethod
    def as_view(cls, **initkwargs):
        view = super(RoomDetail, cls).as_view(**initkwargs)
        return login_required(view, redirect_field_name=None)

    def get(self, request, id):
        room=Room.objects.filter(owner=request.user.member, id=id)
        if room:
            return render(request, 'room_read.html', {'room':room[0]})
        return HttpResponseRedirect(reverse('room'))
    def post(self, request, id):
        return self.get(request, id)
        
class RoomEdit(View):
    @classmethod
    def as_view(cls, **initkwargs):
        view = super(RoomEdit, cls).as_view(**initkwargs)
        return login_required(view, redirect_field_name=None)

    def get(self, request, id):
            room=Room.objects.filter(owner=request.user.member, id=id)
            rc=RoomClass.objects.filter(owner=request.user.member).order_by('-id')
            if room:
                return render(request, 'room_edit.html', {'room':room[0], 'rc':rc})
            return HttpResponseRedirect(reverse('room'))
    def post(self, request, id):
        room=Room.objects.filter(owner=request.user.member, id=id)
        if room:
            form = RoomForm(request.POST, instance=room[0])
            rc=RoomClass.objects.filter(owner=request.user.member).order_by('-id')
            if form.is_valid():
                room=form.save()
                return render(request, 'room_edit.html', {'success':"Data berhasil dirubah", 'room':room, 'rc':rc})
            return render(request, 'room_edit.html', {'error':form.errors, 'room':room[0], 'rc':rc})
        return HttpResponseRedirect(reverse('room'))
        
class RoomDelete(View):
    @classmethod
    def as_view(cls, **initkwargs):
        view = super(RoomDelete, cls).as_view(**initkwargs)
        return login_required(view, redirect_field_name=None)

    def get(self, request, id):
        room=Room.objects.filter(owner=request.user.member, id=id)
        if room:
            return render(request, 'room_delete.html', {'room':room[0]})
        return HttpResponseRedirect(reverse('room'))
    def post(self, request, id):
        room=Room.objects.filter(owner=request.user.member, id=id)
        if room:
            name=room[0].name
            room.delete()
            messages.success(request, 'Data "'+name+'" telah berhasil dihapus.')
        return HttpResponseRedirect(reverse('room'))
        
class RoomClassTable(View):
    @classmethod
    def as_view(cls, **initkwargs):
        view = super(RoomClassTable, cls).as_view(**initkwargs)
        return login_required(view, redirect_field_name=None)

    def get(self, request):
        rc=RoomClass.objects.filter(owner=request.user.member).order_by('-id')
        return render(request, 'rc.html', {'rc':rc})
    def post(self, request):
        form = RoomClassForm(request.POST)
        rc=RoomClass.objects.filter(owner=request.user.member).order_by('-id')
        if form.is_valid():
            new=form.save(commit=False)
            new.owner=request.user.member
            new.save()
            rc=RoomClass.objects.filter(owner=request.user.member).order_by('-id')
            return render(request, 'rc.html', {'success':"Data berhasil ditambahkan", 'rc':rc})
        else:
            return render(request, 'rc.html', {'error':form.errors, 'rc':rc})
            
class RoomClassDetail(View):
    @classmethod
    def as_view(cls, **initkwargs):
        view = super(RoomClassDetail, cls).as_view(**initkwargs)
        return login_required(view, redirect_field_name=None)

    def get(self, request, id):
        rc=RoomClass.objects.filter(owner=request.user.member, id=id)
        if rc:
            return render(request, 'rc_read.html', {'rc':rc[0]})
        return HttpResponseRedirect(reverse('rclass'))
    def post(self, request, id):
        return self.get(request, id)
        
class RoomClassEdit(View):
    @classmethod
    def as_view(cls, **initkwargs):
        view = super(RoomClassEdit, cls).as_view(**initkwargs)
        return login_required(view, redirect_field_name=None)

    def get(self, request, id):
            rc=RoomClass.objects.filter(owner=request.user.member, id=id)
            if rc:
                return render(request, 'rc_edit.html', {'rc':rc[0]})
            return HttpResponseRedirect(reverse('rclass'))
    def post(self, request, id):
        rc=RoomClass.objects.filter(owner=request.user.member, id=id)
        if rc:
            form = RoomClassForm(request.POST, instance=rc[0])
            if form.is_valid():
                rc=form.save()
                return render(request, 'rc_edit.html', {'success':"Data berhasil dirubah", 'rc':rc})
            return render(request, 'rc_edit.html', {'error':form.errors, 'rc':rc[0]})
        return HttpResponseRedirect(reverse('rclass'))
        
class RoomClassDelete(View):
    @classmethod
    def as_view(cls, **initkwargs):
        view = super(RoomClassDelete, cls).as_view(**initkwargs)
        return login_required(view, redirect_field_name=None)

    def get(self, request, id):
        rc=RoomClass.objects.filter(owner=request.user.member, id=id)
        if rc:
            return render(request, 'rc_delete.html', {'rc':rc[0]})
        return HttpResponseRedirect(reverse('rclass'))
    def post(self, request, id):
        rc=RoomClass.objects.filter(owner=request.user.member, id=id)
        if rc:
            name=rc[0].name
            rc.delete()
            messages.success(request, 'Data "'+name+'" telah berhasil dihapus.')
        return HttpResponseRedirect(reverse('rclass'))