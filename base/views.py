from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
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

class load_page(View):

    def get(self, request, page=None, error=None):
        if request.user.is_authenticated():
            if None == page:
                return render(request, 'index.html')
            else:
                return render(request, page + '.html')
        return render(request, 'login.html')
    
    def post(self, request):
        if('login' in request.POST):
            form = LoginForm(request.POST)
            if form.is_valid():
                login = user_auth(request, form.cleaned_data['username'], form.cleaned_data['password'])
                if not login:
                    return render(request, 'login.html', {'error':'Username dan password tidak cocok'})
                else:
                    return render(request, 'index.html')
            else:
                return render(request, 'index.html')

def user_auth(request, username, password):
    user = authenticate(username=username, password=password)
    if user is not None and user.is_active and CareGiver.objects.filter(user=user):
        login(request, user)
    else:
        return False
    return True

def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))


def status(request):
    if request.user.is_authenticated():
        return HttpResponse("Logged in")
    else:
        return HttpResponse("Logged out")
