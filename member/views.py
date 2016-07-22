from rest_framework import viewsets, mixins
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.decorators import list_route, parser_classes
from rest_framework.parsers import FormParser, MultiPartParser
from rest_framework.status import HTTP_400_BAD_REQUEST, HTTP_201_CREATED
from django.http import HttpResponseRedirect
from django.views.generic import View
from django.shortcuts import render
from django.core.urlresolvers import reverse
from member.forms import ElderForm, ElderUserForm, JoinForm, CGUserForm
from member.forms import CareGiverForm, PartnerForm, PartnerUserForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from member.models import Elder, CareGiver, CareGiving, Partner
from django.contrib.auth.models import Group
from django.utils.crypto import get_random_string
from member.serializers import ElderSerializer
from member.serializers import SignupSerializer, CareGiverSerializer
from base.views import cek_session, is_caregiver

from rest_framework.permissions import IsAuthenticated


class Elders(mixins.ListModelMixin,
             mixins.RetrieveModelMixin,
             mixins.UpdateModelMixin,
             mixins.DestroyModelMixin,
             viewsets.GenericViewSet):
    # queryset = Elder.objects.all()
    serializer_class = ElderSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        user = self.request.user
        try:
            cg=user.caregiver
        except:
            try:
                elders=user.elder
            except:
                retval=[]
            else:
                retval=elders
        else:
            retval=cg.elder_set.all()
        return retval
    
    def perform_destroy(self, instance):
        elder = instance
        name = elder.user.first_name + " " + elder.user.last_name
        if elder.cared_by.count() == 1:
            elder.delete()
        else:
            try:
                cg = CareGiver.objects.get(user=self.request.user)
            except CareGiver.DoesNotExist:
                cg = None
            
            if cg:
                CareGiving.objects.filter(
                    elder=elder, caregiver=cg).delete()
                
    @list_route(methods=['POST'])
    def join(self, request, *args, **kwargs):
        if 'phone' in request.data:
            phone = request.data['phone']
            user = self.request.user
            try:
                user.caregiver
            except:
                return Response(status=HTTP_400_BAD_REQUEST)
            else:
                elder = Elder.objects.get(phone=phone)
                CareGiving.objects.create(caregiver=user.caregiver, elder=elder)
                serializer=ElderSerializer(elder)
            return Response(serializer.data)


class CareGivers(mixins.ListModelMixin,
             mixins.RetrieveModelMixin,
             mixins.UpdateModelMixin,
             viewsets.GenericViewSet):
    serializer_class = CareGiverSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        user = self.request.user
        try:
            cg=user.caregiver
        except:
            try:
                elders=user.elder
            except:
                retval=[]
            else:
                retval=elders.cared_by.all()
        else:
            retval=CareGiver.objects.filter(user=user)
        return retval
    
class Profile(viewsets.ViewSet):
    #serializer_class = UserSerializer
    permission_classes = (IsAuthenticated,)

    def list(self, request):
        user = self.request.user
        try:
            user.caregiver
        except:
            try:
                user.elder
            except:
                serializer=UserSerializer(user)
            else:
                serializer=ElderSerializer(user.elder)
        else:
            serializer=CareGiverSerializer(user.caregiver)
        return Response(serializer.data)
    
    @list_route(methods=['POST'])
    @parser_classes((FormParser, MultiPartParser))
    def image(self, request, *args, **kwargs):
        if 'upload' in request.data:
            upload=request.data['upload']
            user = self.request.user
            try:
                user.caregiver
            except:
                try:
                    user.elder
                except:
                    return Response(status=HTTP_400_BAD_REQUEST)
                else:
                    user.elder.photo.delete()
                    user.elder.photo.save(upload.name, upload)
                    serializer=ElderSerializer(user.elder)
            else:
                user.caregiver.photo.delete()
                user.caregiver.photo.save(upload.name, upload)
                serializer=CareGiverSerializer(user.caregiver)

            return Response(serializer.data, status=HTTP_201_CREATED)
        else:
            return Response(status=HTTP_400_BAD_REQUEST)


class Signup(viewsets.GenericViewSet):
    queryset = CareGiver.objects.all()
    serializer_class = SignupSerializer
    permission_classes = (AllowAny,)

    def create(self, request):
        serializer = SignupSerializer(data=request.data,
                                      context={'request': request})
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
        elder = None
        if (request.session.get('active_elder') is not None and
                request.session['active_elder'] != 0):
            elder = Elder.objects.get(pk=request.session.get('active_elder'))
        elders = Elder.get_cared_elder(
            user=CareGiver.objects.get(user=request.user))
        return render(request, 'parents.html',
                      {'elders': elders, 'active_elder': elder})

    def post(self, request):
        cek_session(request)
        elder = None
        if('join' in request.POST):
            form = JoinForm(request.POST, request=request)
            if form.is_valid():
                kode = form.cleaned_data.get('kode')
                elder = Elder.objects.get(code=kode)
                caregiver = CareGiver.objects.get(user=request.user)
                elders = Elder.get_cared_elder(
                    user=CareGiver.objects.get(user=request.user))
                CareGiving.objects.create(caregiver=caregiver, elder=elder)
                if (request.session.get('active_elder') is not None and
                        request.session['active_elder'] != 0):
                    elder = Elder.objects.get(
                        pk=request.session.get('active_elder'))
                return render(
                        request,
                        'parents.html',
                        {'elders': elders,
                            'success': "Orang tua berhasil ditambahkan",
                            'active_elder': elder})
            else:
                if (request.session.get('active_elder') is not None and
                        request.session['active_elder'] != 0):
                    elder = Elder.objects.get(
                        pk=request.session.get('active_elder'))
                elders = Elder.get_cared_elder(
                    user=CareGiver.objects.get(user=request.user))
                return render(
                        request, 'parents.html',
                        {'error_join': form.errors, 'active_elder': elder,
                            'elders': elders})
        elif('add' in request.POST):
            userform = ElderUserForm(request.POST)
            elderform = ElderForm(request.POST, request.FILES)
            alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
            if userform.is_valid() and elderform.is_valid():
                code = get_random_string(length=8, allowed_chars=alphabet)
                while Elder.objects.filter(code=code):
                    code = get_random_string(length=8)
                user = userform.save(commit=False)
                user.username = code
                user.set_password('asdfg4321')
                user.save()
                elder = elderform.save(commit=False)
                elder.user = user
                elder.code = code
                elder.save()
                caregiver = CareGiver.objects.get(user=request.user)
                CareGiving.objects.create(caregiver=caregiver, elder=elder)
                g = Group.objects.get(name='Elder')
                g.user_set.add(user)
                elders = Elder.get_cared_elder(user=caregiver)
                if request.session['active_elder'] == 0:
                    if elders:
                        request.session['active_elder'] = elders[0].id
                    else:
                        request.session['active_elder'] = 0
                elder = Elder.objects.get(
                    pk=request.session.get('active_elder'))
                return render(
                        request,
                        'parents.html',
                        {'elders': elders,
                            'success': "Orang tua berhasil ditambahkan",
                            'active_elder': elder})
            else:
                userform.errors.update(elderform.errors)
                elders = Elder.get_cared_elder(
                    user=CareGiver.objects.get(user=request.user))
                if (request.session.get('active_elder') is not None and
                        request.session['active_elder'] != 0):
                    elder = Elder.objects.get(
                        pk=request.session.get('active_elder'))
                else:
                    elder = None
                return render(
                        request,
                        'parents.html',
                        {'elders': elders, 'error': userform.errors,
                            'active_elder': elder})
        else:
            return self.get(request)


class UpdateElder(View):

    @classmethod
    def as_view(cls, **initkwargs):
        view = super(UpdateElder, cls).as_view(**initkwargs)
        return login_required(view, redirect_field_name=None)

    def get(self, request, id):
        if is_caregiver(request.user):
            cek_session(request)
            active = None
            if (request.session.get('active_elder') is not None and
                    request.session['active_elder'] != 0):
                active = Elder.objects.get(
                    pk=request.session.get('active_elder'))
            elders = Elder.get_cared_elder(
                user=CareGiver.objects.get(user=request.user))
            elder = elders.filter(id=id)
            if elder:
                return render(
                        request,
                        'parents_edit.html',
                        {'elders': elders, 'active_elder': active,
                            'edit': elder[0]})
            return HttpResponseRedirect(reverse('parents'))
        else:
            return HttpResponseRedirect(reverse('index'))

    def post(self, request, id):
        if is_caregiver(request.user):
            cek_session(request)
            active = None
            if request.session.get('active_elder') is not None and \
               request.session['active_elder'] != 0:
                active = Elder.objects.get(
                    pk=request.session.get('active_elder'))
            elders = Elder.get_cared_elder(
                user=CareGiver.objects.get(user=request.user))
            elder = elders.filter(id=id)
            if elder:
                userform = ElderUserForm(request.POST, instance=elder[0].user)
                elderform = ElderForm(
                    request.POST, request.FILES, instance=elder[0])
                if userform.is_valid() and elderform.is_valid():
                    userform.save()
                    elder = elderform.save()
                    return render(request, 'parents_edit.html',
                                  {'elders': elders,
                                   'success': "Data tersimpan",
                                   'active_elder': active, 'edit': elder})
                else:
                    userform.errors.update(elderform.errors)
                    return render(request, 'parents_edit.html',
                                  {'elders': elders, 'error': userform.errors,
                                   'active_elder': active, 'edit': elder[0]})
            return HttpResponseRedirect(reverse('parents'))
        else:
            return HttpResponseRedirect(reverse('index'))


class DeleteElder(View):

    @classmethod
    def as_view(cls, **initkwargs):
        view = super(DeleteElder, cls).as_view(**initkwargs)
        return login_required(view, redirect_field_name=None)

    def get(self, request, id):
        cek_session(request)
        active = None
        if request.session.get('active_elder') is not None and \
           request.session['active_elder'] != 0:
            active = Elder.objects.get(pk=request.session.get('active_elder'))
        elders = Elder.get_cared_elder(
            user=CareGiver.objects.get(user=request.user))
        elder = elders.filter(id=id)
        if elder:
            return render(request, 'parents_delete.html',
                          {'elders': elders, 'active_elder': active,
                           'delete': elder[0]})
        return HttpResponseRedirect(reverse('parents'))

    def post(self, request, id):
        cek_session(request)
        elders = Elder.get_cared_elder(
            user=CareGiver.objects.get(user=request.user))
        elder = elders.filter(id=id)
        if elder:
            elder = elder[0]
            name = elder.user.first_name + " " + elder.user.last_name
            if elder.cared_by.count() == 1:
                elder.delete()
            else:
                cg = CareGiver.objects.get(user=request.user)
                CareGiving.objects.filter(
                    elder=elder, caregiver=cg).delete()
            if int(id) == request.session.get('active_elder'):
                elders = Elder.get_cared_elder(
                    user=CareGiver.objects.get(user=request.user))
                if elders:
                    request.session['active_elder'] = elders[0].id
                else:
                    request.session['active_elder'] = 0
            messages.success(
                request, name + ' berhasil dihapus dari daftar anda.')
        return HttpResponseRedirect(reverse('parents'))


@login_required(redirect_field_name=None)
def set_active_elder(request, id):
    cg = CareGiver.objects.get(user=request.user)
    cared = Elder.get_cared_elder(user=cg)
    if cared.filter(id=id):
        request.session['active_elder'] = int(id)
    return HttpResponseRedirect(request.GET.get('next', '/'))


class UpdateProfile(View):

    @classmethod
    def as_view(cls, **initkwargs):
        view = super(UpdateProfile, cls).as_view(**initkwargs)
        return login_required(view, redirect_field_name=None)

    def get(self, request):
        if is_caregiver(request.user):
            cek_session(request)
            active = None
            if request.session.get('active_elder') is not None and \
               request.session['active_elder'] != 0:
                active = Elder.objects.get(
                    pk=request.session.get('active_elder'))
            elders = Elder.get_cared_elder(
                user=CareGiver.objects.get(user=request.user))
            return render(request, 'profile_edit.html',
                          {'elders': elders, 'active_elder': active})
        else:
            return render(request, 'partnerprofile_edit.html')

    def post(self, request):
        if is_caregiver(request.user):
            cek_session(request)
            active = None
            if request.session.get('active_elder') is not None and \
               request.session['active_elder'] != 0:
                active = Elder.objects.get(
                    pk=request.session.get('active_elder'))
            elders = Elder.get_cared_elder(
                user=CareGiver.objects.get(user=request.user))
            userform = CGUserForm(request.POST, instance=request.user)
            cgform = CareGiverForm(
                request.POST, request.FILES,
                instance=CareGiver.objects.get(user=request.user))
            if userform.is_valid() and cgform.is_valid():
                userform.save()
                cgform.save()
                return render(request, 'profile_edit.html',
                              {'elders': elders, 'success': "Data tersimpan",
                               'active_elder': active})
            else:
                userform.errors.update(cgform.errors)
                return render(request, 'profile_edit.html',
                              {'elders': elders, 'error': userform.errors,
                               'active_elder': active})
        else:
            userform = PartnerUserForm(request.POST, instance=request.user)
            partnerform = PartnerForm(
                request.POST, request.FILES,
                instance=Partner.objects.get(user=request.user))
            if userform.is_valid() and partnerform.is_valid():
                userform.save()
                partnerform.save()
                return render(request, 'partnerprofile_edit.html',
                              {'success': "Data tersimpan"})
            else:
                userform.errors.update(partnerform.errors)
                return render(request, 'partnerprofile_edit.html',
                              {'error': userform.errors})
