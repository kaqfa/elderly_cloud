from django.shortcuts import render
from django.contrib.auth import login, logout
from django.contrib.auth.models import Group, User
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.views.generic import View

from rest_framework import viewsets
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.serializers import AuthTokenSerializer
from base.serializers import LoginSerializer
from rest_framework.decorators import list_route
from rest_framework.response import Response
from member.models import CareGiver, Elder
from base.forms import LoginForm
from member.forms import CareGiverForm, UserForm
from member.serializers import ElderSerializer, CareGiverSerializer
from info.models import Posting
from datetime import datetime, date, time
from datetime import timedelta
from tracker.models import Tracker
from article.models import Article


def redirect(request):
    return HttpResponseRedirect(reverse('index'))

def is_caregiver(user):
    if CareGiver.objects.filter(user=user):
        return True
    else:
        return False


def cek_session(request):
    if 'active_elder' not in request.session:
        elders = Elder.get_cared_elder(
            user=CareGiver.objects.get(user=request.user))
        if elders:
            request.session['active_elder'] = elders[0].id
        else:
            request.session['active_elder'] = 0


class Login(viewsets.GenericViewSet):
    serializer_class = LoginSerializer
    permission_classes = ()

    def create(self, request):
        serializer = AuthTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        if CareGiver.objects.filter(user=user):
            token, created = Token.objects.get_or_create(user=user)
            caregiver= CareGiver.objects.get(user=user)
            serializer=CareGiverSerializer(caregiver)
            return Response({'token': token.key, 'profile':serializer.data})
        else:
            return Response({'non_field_errors':
                             ["username dan password tidak tepat"]})

    @list_route(methods=['post'])
    def elder(self, request):
        if request.data.get('phone') is None or request.data.get('phone') == '':
            return Response({'phone': ["This field is required."]}, status=400)
        else:
            phone = request.data.get('phone')
            elder = Elder.objects.filter(phone=phone)
            if elder:
                elder = elder[0]
                token, created = Token.objects.get_or_create(user=elder.user)
                elder= Elder.objects.get(user=elder.user)
                serializer=ElderSerializer(elder)
                return Response({'token': token.key, 'profile':serializer.data})
            else:
                return Response({'non_field_errors':
                                 ['username dan password tidak tepat.']}, status=400)


class Index(View):

    def get(self, request, page=None):
        print('index')
        if request.user.is_authenticated():
            if request.user.is_superuser:
                return HttpResponseRedirect(reverse('admin:index'))
            elif is_caregiver(request.user):
                cek_session(request)
                return self.caregiver(request)
            else:
                return self.partner(request)
        else:
            return render(request, 'login.html')

    def post(self, request):
        if('login' in request.POST):
            form = LoginForm(request.POST)            
            if form.is_valid():
                user = form.login(request)                
                if user:                    
                    login(request, user)                    
                    if is_caregiver(user):
                        caregiver = CareGiver.objects.get(user=user)
                        elders = Elder.get_cared_elder(caregiver)
                        if elders:
                            request.session['active_elder'] = elders[0].id
                        else:
                            request.session['active_elder'] = 0
                        return self.caregiver(request)
                    else:                        
                        return self.partner(request)
            else:                                
                return render(request, 'login.html',
                              {'error_login': form.errors})

        elif('signup' in request.POST):
            userform = UserForm(request.POST)
            caregiverform = CareGiverForm(request.POST)
            # return reverse(request.POST['gender'])
            if userform.is_valid() and caregiverform.is_valid():
                user = userform.save(commit=False)
                user.set_password(userform.cleaned_data.get('password'))
                user.save()
                caregiver = caregiverform.save(commit=False)
                caregiver.user = user
                caregiver.save()
                g = Group.objects.get(name='CareGiver')
                g.user_set.add(user)
                return render(request, 'login.html',
                              {'success':
                               "Pendaftaran Berhasil, silahkan login"})
            else:
                userform.errors.update(caregiverform.errors)
                return render(request, 'login.html',
                              {'error_signup': userform.errors,
                               'values': request.POST})
        else:
            return render(request, 'login.html')

    def caregiver(self, request):
        posting = None  # Posting.get_latest_post()
        if request.session['active_elder'] != 0:
            elder = Elder.objects.get(pk=request.session.get('active_elder'))
            caregiver = CareGiver.objects.get(user=request.user)
            today = datetime.combine(date.today(), time.min)
            lastweek = today - timedelta(days=7)
            tracker = elder.tracker_set.filter(created__gte=lastweek)
            blood = tracker.filter(type="bg")
            heartrate = tracker.filter(type="hr")
            daily_condition = tracker.filter(type="cd")
            elders = Elder.get_cared_elder(
                user=CareGiver.objects.get(user=request.user))
            return render(request, 'index.html',
                          {'active_elder': elder, 'elders': elders,
                           'info': posting, 'caregiver': caregiver,
                           'blood': blood, 'heartrate': heartrate,
                           'daily_condition': daily_condition})
        else:
            caregiver = CareGiver.objects.get(user=request.user)
            elders = Elder.get_cared_elder(
                user=CareGiver.objects.get(user=request.user))
            return render(
                request,
                'index.html', {'caregiver': caregiver, 'elders': elders})

    def partner(self, request):
        today = datetime.now().date()
        today_start = datetime.combine(today, time())
        allUsers = User.objects.filter(is_staff = 0, is_active = 1).count()
        caregivers = CareGiver.objects.all().count()
        elders = Elder.objects.all().count()
        todayTrackers = Tracker.objects.filter(created__gte = today_start).values_list('elder_id', flat = True)
        notToday = Elder.objects.exclude(user_id = todayTrackers)
        articles = Article.objects.all()
        return render(request, 'partner/index.html', 
                      {'all': allUsers, 'caregivers': caregivers, 
                       'elders': elders, 'notToday': notToday, 'articles': articles})


def user_logout(request):
    # pass
    print("logout")
    logout(request)
    return HttpResponseRedirect(reverse('index'))


def status(request):
    print ("status")
    if request.user.is_authenticated():        
        return HttpResponse("Logged in")
    else:
        return HttpResponse("Logged out")
