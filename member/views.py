from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from django.http import HttpResponseRedirect
from django.views.generic import View
from django.shortcuts import render
from django.core.urlresolvers import reverse
from member.forms import ElderForm, ElderUserForm, JoinForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages


from member.models import Elder, CareGiver, Member, CareGiving
from django.contrib.auth.models import Group
from django.utils.crypto import get_random_string
from member.serializers import ElderSerializer, SignupSerializer, CareGiverSerializer
from base.views import cek_session


class Elders(viewsets.ReadOnlyModelViewSet):
    queryset = Elder.objects.all()
    serializer_class = ElderSerializer


class Signup(viewsets.GenericViewSet):
    queryset = Member.objects.all()
    serializer_class = SignupSerializer
    permission_classes = (AllowAny,)

    def create(self, request):
        serializer = SignupSerializer(data=request.data)
        if serializer.is_valid():
            signup_data = serializer.save()
            if type(signup_data) is Elder:
                serializer = ElderSerializer(signup_data)
            elif type(signup_data) is CareGiver:
                serializer = CareGiverSerializer(signup_data)
            else:
                return Response(serializer.errors, status=400)
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

class Parents(View):
    
    @classmethod
    def as_view(cls, **initkwargs):
        view = super(Parents, cls).as_view(**initkwargs)
        return login_required(view, redirect_field_name=None)

    def get(self, request):
        cek_session(request)
        elder=None
        if request.session.get('active_elder') is not None and request.session['active_elder']!=0:
            elder=Elder.objects.get(pk=request.session.get('active_elder'))
        elders=Elder.get_cared_elder(user=CareGiver.objects.get(user=request.user))
        return render(request, 'parents.html', {'elders':elders, 'active_elder':elder})
    
    def post(self, request):
        cek_session(request)
        elder=None
        if('join' in request.POST):
            form = JoinForm(request.POST, request=request)
            if form.is_valid():
                kode=form.cleaned_data.get('kode')
                elder=Elder.objects.get(code=kode)
                caregiver = CareGiver.objects.get(user=request.user)
                elders=Elder.get_cared_elder(user=CareGiver.objects.get(user=request.user))
                CareGiving.objects.create(caregiver=caregiver, elder=elder)
                if request.session.get('active_elder') is not None and request.session['active_elder']!=0:
                    elder=Elder.objects.get(pk=request.session.get('active_elder'))
                return render(request, 'parents.html', {'elders':elders, 'success': "Orang tua berhasil ditambahkan", 'active_elder':elder})
            else:
                if request.session.get('active_elder') is not None and request.session['active_elder']!=0:
                    elder=Elder.objects.get(pk=request.session.get('active_elder'))
                elders=Elder.get_cared_elder(user=CareGiver.objects.get(user=request.user))
                return render(request, 'parents.html', {'error_join':form.errors, 'active_elder':elder, 'elders': elders})
        elif('add' in request.POST):
            userform = ElderUserForm(request.POST)
            elderform = ElderForm(request.POST, request.FILES)
            if userform.is_valid() and elderform.is_valid():
                code = get_random_string(length=8, allowed_chars="ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789")
                while Elder.objects.filter(code=code):
                    code = get_random_string(length=8)
                user = userform.save(commit=False)
                user.username=code
                user.set_password('asdfg4321')
                user.save()
                elder = elderform.save(commit=False)
                elder.user=user
                elder.code=code
                elder.save()
                caregiver = CareGiver.objects.get(user=request.user)
                CareGiving.objects.create(caregiver=caregiver, elder=elder)
                g = Group.objects.get(name='Elder')
                g.user_set.add(user)
                if request.session.get('active_elder') is not None and request.session['active_elder']!=0:
                    elder=Elder.objects.get(pk=request.session.get('active_elder'))
                elders=Elder.get_cared_elder(user=caregiver)
                return render(request, 'parents.html', {'elders':elders, 'success': "Orang tua berhasil ditambahkan", 'active_elder':elder})
            else:
                userform.errors.update(elderform.errors)
                elders=Elder.get_cared_elder(user=CareGiver.objects.get(user=request.user))
                if request.session.get('active_elder') is not None and request.session['active_elder']!=0:
                    elder=Elder.objects.get(pk=request.session.get('active_elder'))
                return render(request, 'parents.html', {'elders':elders, 'error':userform.errors, 'active_elder':elder})
        else:
            return self.get(request)
            
class UpdateElder(View):
    
    @classmethod
    def as_view(cls, **initkwargs):
        view = super(UpdateElder, cls).as_view(**initkwargs)
        return login_required(view, redirect_field_name=None)

    def get(self, request, id):
        cek_session(request)
        active=None
        if request.session.get('active_elder') is not None and request.session['active_elder']!=0:
            active=Elder.objects.get(pk=request.session.get('active_elder'))
        elders=Elder.get_cared_elder(user=CareGiver.objects.get(user=request.user))
        elder=elders.filter(id=id)
        if elder:
            return render(request, 'parents_edit.html', {'elders':elders, 'active_elder':active, 'edit':elder[0]})
        return HttpResponseRedirect(reverse('parents'))
    
    def post(self, request, id):
        cek_session(request)
        active=None
        if request.session.get('active_elder') is not None and request.session['active_elder']!=0:
            active=Elder.objects.get(pk=request.session.get('active_elder'))
        elders=Elder.get_cared_elder(user=CareGiver.objects.get(user=request.user))
        elder=elders.filter(id=id)
        if elder:
            userform = ElderUserForm(request.POST, instance=elder[0].user)
            elderform = ElderForm(request.POST, request.FILES, instance=elder[0])
            if userform.is_valid() and elderform.is_valid():
                user = userform.save()
                elder = elderform.save()
                return render(request, 'parents_edit.html', {'elders':elders, 'success': "Data tersimpan", 'active_elder':active, 'edit':elder})
            else:
                userform.errors.update(elderform.errors)            
                return render(request, 'parents_edit.html', {'elders':elders, 'error':userform.errors, 'active_elder':active, 'edit':elder[0]})
        return HttpResponseRedirect(reverse('parents'))
            
class DeleteElder(View):
    @classmethod
    def as_view(cls, **initkwargs):
        view = super(DeleteElder, cls).as_view(**initkwargs)
        return login_required(view, redirect_field_name=None)

    def get(self, request, id):
        cek_session(request)
        active=None
        if request.session.get('active_elder') is not None and request.session['active_elder']!=0:
            active=Elder.objects.get(pk=request.session.get('active_elder'))
        elders=Elder.get_cared_elder(user=CareGiver.objects.get(user=request.user))
        elder=elders.filter(id=id)
        if elder:
            return render(request, 'parents_delete.html', {'elders':elders, 'active_elder':active, 'delete':elder[0]})
        return HttpResponseRedirect(reverse('parents'))
    
    def post(self, request, id):
        cek_session(request)
        active=None
        if request.session.get('active_elder') is not None and request.session['active_elder']!=0:
            active=Elder.objects.get(pk=request.session.get('active_elder'))
        elders=Elder.get_cared_elder(user=CareGiver.objects.get(user=request.user))
        elder=elders.filter(id=id)
        if elder:
            elder=elder[0]
            name=elder.user.first_name+" "+elder.user.last_name
            if elder.cared_by.count()==1:
                elder.delete()
            else:
                CareGiving.objects.filter(elder=elder, caregiver=CareGiver.objects.get(user=request.user)).delete()
            if id==request.session.get('active_elder'):
                elders=Elder.get_cared_elder(user=CareGiver.objects.get(user=request.user))
                request.session['active_elder']=elders[0].id
            messages.success(request, name+' berhasil dihapus dari daftar anda.')
        return HttpResponseRedirect(reverse('parents'))
                
        
@login_required(redirect_field_name=None)
def set_active_elder(request, id):
    if Elder.get_cared_elder(user=CareGiver.objects.get(user=request.user)).filter(id=id):
        request.session['active_elder']=id
    return HttpResponseRedirect(request.GET.get('next', '/'))