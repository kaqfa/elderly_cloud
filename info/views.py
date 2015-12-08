from rest_framework import viewsets

from info.models import Posting, PointOfInterest
from info.forms import CommentForm
from info.serializers import PostingSerializer
from django.views.generic import View
from django.shortcuts import render
from django.core.urlresolvers import reverse
from base.views import cek_session
from member.models import Elder, CareGiver
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.http import HttpResponseRedirect, HttpResponse


# Create your views here.

class infos(viewsets.ReadOnlyModelViewSet):
    queryset = Posting.objects.all()
    serializer_class = PostingSerializer
    
class InfoAll(View):
    @classmethod
    def as_view(cls, **initkwargs):
        view = super(InfoAll, cls).as_view(**initkwargs)
        return login_required(view, redirect_field_name=None)

    def get(self, request, page=1):
        cek_session(request)
        elder=None
        if request.session.get('active_elder') is not None and request.session['active_elder']!=0:
            elder=Elder.objects.get(pk=request.session.get('active_elder'))
        elders=Elder.get_cared_elder(user=CareGiver.objects.get(user=request.user))
        info=Posting.objects.filter(category__iexact='info').order_by('-id')
        #p=Paginator(info,10)
        #info=p.page(page)
        return render(request, 'post.html', {'elders':elders, 'active_elder':elder, 'tag':'info', 'title':'Info', 'info':info, 'current':page})
    def post(self, request, page=1):
        return self.get(request, page)

class TipsAll(View):
    @classmethod
    def as_view(cls, **initkwargs):
        view = super(TipsAll, cls).as_view(**initkwargs)
        return login_required(view, redirect_field_name=None)

    def get(self, request, page=1):
        cek_session(request)
        elder=None
        if request.session.get('active_elder') is not None and request.session['active_elder']!=0:
            elder=Elder.objects.get(pk=request.session.get('active_elder'))
        elders=Elder.get_cared_elder(user=CareGiver.objects.get(user=request.user))
        info=Posting.objects.filter(category__iexact='tips').order_by('-id')
        #p=Paginator(info,10)
        #info=p.page(page)
        return render(request, 'post.html', {'elders':elders, 'active_elder':elder, 'tag':'tips', 'title':'Tips dan Trik', 'info':info, 'current':page})
    def post(self, request, page=1):
        return self.get(request, page)
        
class PostDetail(View):
    @classmethod
    def as_view(cls, **initkwargs):
        view = super(PostDetail, cls).as_view(**initkwargs)
        return login_required(view, redirect_field_name=None)

    def get(self, request, type, id):
        cek_session(request)
        elder=None
        if request.session.get('active_elder') is not None and request.session['active_elder']!=0:
            elder=Elder.objects.get(pk=request.session.get('active_elder'))
        elders=Elder.get_cared_elder(user=CareGiver.objects.get(user=request.user))
        info=Posting.objects.filter(category=type, id=id)
        if info:
            return render(request, 'post_view.html', {'elders':elders, 'tag':type, 'active_elder':elder, 'info':info[0]})
        return HttpResponseRedirect(reverse(type))
    def post(self, request, type, id):
        cek_session(request)
        elder=None
        if request.session.get('active_elder') is not None and request.session['active_elder']!=0:
            elder=Elder.objects.get(pk=request.session.get('active_elder'))
        elders=Elder.get_cared_elder(user=CareGiver.objects.get(user=request.user))
        info=Posting.objects.filter(category=type, id=id)
        if info:
            form = CommentForm(request.POST)
            if form.is_valid():
                comment = form.save(commit=False)
                comment.owner=request.user
                comment.posting=info[0]
                comment.save()
                return render(request, 'post_view.html', {'elders':elders, 'tag':type, 'active_elder':elder, 'success':'Komentar berhasil ditambahkan', 'info':info[0]})
            return render(request, 'post_view.html', {'elders':elders, 'tag':type, 'active_elder':elder, 'error':form.errors, 'info':info[0]})
        return HttpResponseRedirect(reverse(type))
        
class POIList(View):
    @classmethod
    def as_view(cls, **initkwargs):
        view = super(POIList, cls).as_view(**initkwargs)
        return login_required(view, redirect_field_name=None)

    def get(self, request):
        cek_session(request)
        elder=None
        if request.session.get('active_elder') is not None and request.session['active_elder']!=0:
            elder=Elder.objects.get(pk=request.session.get('active_elder'))
        elders=Elder.get_cared_elder(user=CareGiver.objects.get(user=request.user))
        location=PointOfInterest.objects.order_by('category')
        return render(request, 'location.html', {'elders':elders, 'active_elder':elder, 'location':location})
    def post(self, request):
        return self.get(request)