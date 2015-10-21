from django.shortcuts import render
from django.contrib.auth import login, logout
from django.contrib.auth.models import Group
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.views.generic import View

"""
Authentication Start
"""
from rest_framework import viewsets
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.serializers import AuthTokenSerializer
from base.serializers import LoginSerializer
from rest_framework.decorators import list_route
from rest_framework.response import Response
from member.models import CareGiver, Elder
from base.forms import LoginForm
from member.forms import CareGiverForm, UserForm
from datetime import datetime, date, time
from datetime import timedelta


class Login(viewsets.GenericViewSet):
    serializer_class = LoginSerializer
    permission_classes = ()

    def create(self, request):
        serializer = AuthTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        if CareGiver.objects.filter(user=user):
            token, created = Token.objects.get_or_create(user=user)
            return Response({'token': token.key})
        else:
            return Response({'non_field_errors': ["Unable to log in with provided credentials."]})

    @list_route(methods=['post'])
    def elder(self, request):
        if request.data.get('code') is None or request.data.get('code') == '':
            return Response({'code': ["This field is required."]})
        else:
            code = request.data.get('code')
            elder = Elder.objects.filter(code=code)
            if elder:
                elder = elder[0]
                token, created = Token.objects.get_or_create(user=elder.user)
                return Response({'token': token.key})
            else:
                return Response({'non_field_errors': ['Unable to log in with provided credentials.']})


"""
Authentication End
"""

class Index(View):

    def get(self, request, page=None, error=None):
        if request.user.is_authenticated():
            if None == page:
                if request.session.get('active_elder') is not None and request.session['active_elder']!=0:
                    elder=Elder.objects.get(pk=request.session.get('active_elder'))
                    caregiver=CareGiver.objects.get(user=request.user)
                    today=datetime.combine(date.today(), time.min)
                    lastweek=today-timedelta(days=7)
                    tracker=elder.tracker_set.filter(created__gte=lastweek)
                    blood=tracker.filter(type="bg")
                    heartrate=tracker.filter(type="hr")
                    daily_condition=tracker.filter(type="cd")
                    elders=Elder.get_cared_elder(user=CareGiver.objects.get(user=request.user))
                    return render(request, 'index.html', {'active_elder':elder, 'elders':elders, 'caregiver':caregiver, 'blood':blood, 'heartrate':heartrate, 'daily_condition':daily_condition})
                else:
                    caregiver=CareGiver.objects.get(user=request.user)
                    elders=Elder.get_cared_elder(user=CareGiver.objects.get(user=request.user))
                    return render(request, 'index.html', {'caregiver':caregiver, 'elders':elders})
            else:
                return render(request, page + '.html')
        return render(request, 'login.html')
    
    def post(self, request):
        if('login' in request.POST):
            form = LoginForm(request.POST)
            if form.is_valid():
                user = form.login(request)
                if user:
                    login(request, user)
                    caregiver=CareGiver.objects.get(user=user)
                    elders=Elder.get_cared_elder(caregiver)
                    if elders:
                        request.session['active_elder']=elders[0].id
                        today=datetime.combine(date.today(), time.min)
                        lastweek=today-timedelta(days=7)
                        tracker=elders[0].tracker_set.filter(created__gte=lastweek)
                        blood=tracker.filter(type="bg")
                        heartrate=tracker.filter(type="hr")
                        daily_condition=tracker.filter(type="cd")
                        return render(request, 'index.html', {'active_elder':elders[0], 'elders':elders, 'caregiver':caregiver, 'blood':blood, 'heartrate':heartrate, 'daily_condition':daily_condition})
                    else:
                        request.session['active_elder']=0
                        return render(request, 'index.html', {'elders':elders})
            else:
                return render(request, 'login.html', {'error_login':form.errors})
        elif('signup' in request.POST):
            userform = UserForm(request.POST)
            caregiverform = CareGiverForm(request.POST)
            if userform.is_valid() and caregiverform.is_valid():
                user = userform.save(commit=False)
                user.set_password(userform.cleaned_data.get('password'))
                user.save()
                caregiver = caregiverform.save(commit=False)
                caregiver.user=user
                caregiver.save()
                g = Group.objects.get(name='CareGiver')
                g.user_set.add(user)
                return render(request, 'login.html', {'success': "Pendaftaran Berhasil, silahkan login"})
            else:
                userform.errors.update(caregiverform.errors)
                return render(request, 'login.html', {'error_signup':userform.errors})
        else:
            return render(request, 'login.html')

def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))


def status(request):
    if request.user.is_authenticated():
        return HttpResponse("Logged in")
    else:
        return HttpResponse("Logged out")
