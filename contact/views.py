from rest_framework import viewsets

from contact.models import Contact
from contact.forms import ContactForm
from contact.serializers import ContactSerializer
from member.models import CareGiver, Elder

from django.views.generic import View
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from base.views import cek_session
from django.shortcuts import render
from django.contrib import messages
from django.db.models import Q
# Create your views here.

class contacts(viewsets.ModelViewSet):
    serializer_class = ContactSerializer

    def get_queryset(self):
        if self.request.user.is_authenticated():
            if CareGiver.objects.filter(user=self.request.user):
                caregiver = CareGiver.objects.get(user=self.request.user)
                return Contact.objects.filter(elder__in=Elder.get_cared_elder(caregiver))
            elif Elder.objects.filter(user=self.request.user):
                elder = Elder.objects.get(user=self.request.user)
                return Contact.objects.filter(elder=elder)
        return Contact.objects.all()

class ContactTable(View):
    @classmethod
    def as_view(cls, **initkwargs):
        view = super(ContactTable, cls).as_view(**initkwargs)
        return login_required(view, redirect_field_name=None)

    def get(self, request):
        cek_session(request)
        elder=None
        if request.session.get('active_elder') is not None and request.session['active_elder']!=0:
            elder=Elder.objects.get(pk=request.session.get('active_elder'))
            elders=Elder.get_cared_elder(user=CareGiver.objects.get(user=request.user))
            contact=Contact.objects.filter(elder=elder).order_by('-id')
            return render(request, 'contact.html', {'elders':elders, 'active_elder':elder, 'contact':contact})
        else:
            return HttpResponseRedirect(reverse('index'))
    def post(self, request):
        cek_session(request)
        elder=None
        if request.session.get('active_elder') is not None and request.session['active_elder']!=0:
            elder=Elder.objects.get(pk=request.session.get('active_elder'))
            caregiver=CareGiver.objects.get(user=request.user)
            elders=Elder.get_cared_elder(user=caregiver)
            form = ContactForm(request.POST)
            contact=Contact.objects.filter(elder=elder).order_by('-id')
            if form.is_valid():
                new=form.save(commit=False)
                new.elder=elder
                new.added_by=caregiver
                new.save()
                contact=Contact.objects.filter(elder=elder).order_by('-id')
                return render(request, 'contact.html', {'elders':elders, 'success':"Data berhasil ditambahkan", 'active_elder':elder, 'contact':contact})
            else:
                return render(request, 'contact.html', {'elders':elders, 'error':form.errors, 'active_elder':elder, 'contact':contact})
        else:
            return HttpResponseRedirect(reverse('index'))
            
class ContactDetail(View):
    @classmethod
    def as_view(cls, **initkwargs):
        view = super(ContactDetail, cls).as_view(**initkwargs)
        return login_required(view, redirect_field_name=None)

    def get(self, request, id):
        cek_session(request)
        if request.session.get('active_elder') is not None and request.session['active_elder']!=0:
            elder=Elder.objects.get(pk=request.session.get('active_elder'))
            elders=Elder.get_cared_elder(user=CareGiver.objects.get(user=request.user))
            contact=Contact.objects.filter(elder=elder, id=id)
            if contact:
                return render(request, 'contact_read.html', {'elders':elders, 'active_elder':elder, 'contact':contact[0]})
            return HttpResponseRedirect(reverse('contact'))
        return HttpResponseRedirect(reverse('index'))
    def post(self, request, id):
        return self.get(request, id)
        
class ContactEdit(View):
    @classmethod
    def as_view(cls, **initkwargs):
        view = super(ContactEdit, cls).as_view(**initkwargs)
        return login_required(view, redirect_field_name=None)

    def get(self, request, id):
        cek_session(request)
        if request.session.get('active_elder') is not None and request.session['active_elder']!=0:
            elder=Elder.objects.get(pk=request.session.get('active_elder'))
            elders=Elder.get_cared_elder(user=CareGiver.objects.get(user=request.user))
            contact=Contact.objects.filter(elder=elder, id=id, added_by=CareGiver.objects.get(user=request.user))
            if contact:
                return render(request, 'contact_edit.html', {'elders':elders, 'active_elder':elder, 'contact':contact[0]})
            return HttpResponseRedirect(reverse('contact'))
        return HttpResponseRedirect(reverse('index'))
    def post(self, request, id):
        cek_session(request)
        if request.session.get('active_elder') is not None and request.session['active_elder']!=0:
            elder=Elder.objects.get(pk=request.session.get('active_elder'))
            elders=Elder.get_cared_elder(user=CareGiver.objects.get(user=request.user))
            contact=Contact.objects.filter(elder=elder, id=id, added_by=CareGiver.objects.get(user=request.user))
            if contact:
                form = ContactForm(request.POST, instance=contact[0])
                if form.is_valid():
                    contact=form.save()
                    return render(request, 'contact_edit.html', {'elders':elders, 'success':"Data berhasil dirubah", 'active_elder':elder, 'contact':contact})
                return render(request, 'contact_edit.html', {'elders':elders, 'active_elder':elder, 'error':form.errors, 'contact':contact[0]})
            return HttpResponseRedirect(reverse('contact'))
        return HttpResponseRedirect(reverse('index'))
        
class ContactDelete(View):
    @classmethod
    def as_view(cls, **initkwargs):
        view = super(ContactDelete, cls).as_view(**initkwargs)
        return login_required(view, redirect_field_name=None)

    def get(self, request, id):
        cek_session(request)
        if request.session.get('active_elder') is not None and request.session['active_elder']!=0:
            elder=Elder.objects.get(pk=request.session.get('active_elder'))
            elders=Elder.get_cared_elder(user=CareGiver.objects.get(user=request.user))
            contact=Contact.objects.filter(elder=elder, id=id, added_by=CareGiver.objects.get(user=request.user))
            if contact:
                return render(request, 'contact_delete.html', {'elders':elders, 'active_elder':elder, 'contact':contact[0]})
            return HttpResponseRedirect(reverse('contact'))
        return HttpResponseRedirect(reverse('index'))
    def post(self, request, id):
        cek_session(request)
        if request.session.get('active_elder') is not None and request.session['active_elder']!=0:
            elder=Elder.objects.get(pk=request.session.get('active_elder'))
            elders=Elder.get_cared_elder(user=CareGiver.objects.get(user=request.user))
            contact=Contact.objects.filter(elder=elder, id=id, added_by=CareGiver.objects.get(user=request.user))
            if contact:
                name=contact[0].name
                contact.delete()
                messages.success(request, 'Data "'+name+'" telah berhasil dihapus.')
        return HttpResponseRedirect(reverse('contact'))