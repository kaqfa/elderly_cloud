from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse


def load_page(request, page=None):
    if page == None:
        return render(request, 'index.html')

    return render(request, page + '.html')


def user_auth(request):
    user = authenticate(username='john', password='johnpassword')
    login(request, user)
    return HttpResponseRedirect(reverse('status'))


def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('status'))


def status(request):
    if request.user.is_authenticated():
        return HttpResponse("Logged in")
    else:
        return HttpResponse("Logged out")