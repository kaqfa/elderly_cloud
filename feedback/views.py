# Create your views here.
from member.models import Elder, CareGiver
from django.db.models import Q
from django.views.generic import View
from base.views import cek_session
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import HttpResponseRedirect

from feedback.models import Feedback, Response
from feedback.forms import FeedbackForm, ResponseForm
from django.core.urlresolvers import reverse
from django.contrib import messages

class FeedbackList(View):
    @classmethod
    def as_view(cls, **initkwargs):
        view = super(FeedbackList, cls).as_view(**initkwargs)
        return login_required(view, redirect_field_name=None)

    def get(self, request):
        cek_session(request)
        elder=None
        if request.session.get('active_elder') is not None and request.session['active_elder']!=0:
            elder=Elder.objects.get(pk=request.session.get('active_elder'))
        elders=Elder.get_cared_elder(user=CareGiver.objects.get(user=request.user))
        feedback=Feedback.objects.filter(owner=request.user)
        return render(request, 'feedback.html', {'elders':elders, 'active_elder':elder, 'feedback':feedback})
    
    def post(self, request):
        cek_session(request)
        elder=None
        if request.session.get('active_elder') is not None and request.session['active_elder']!=0:
            elder=Elder.objects.get(pk=request.session.get('active_elder'))
        elders=Elder.get_cared_elder(user=CareGiver.objects.get(user=request.user))
        feedback=Feedback.objects.filter(owner=request.user)
        form=FeedbackForm(request.POST)
        if form.is_valid():
            new=form.save(commit=False)
            new.status='s'
            new.owner=request.user
            new.save()
            feedback=Feedback.objects.filter(owner=request.user)
            return render(request, 'feedback.html', {'elders':elders, 'success':'Feedback berhasil ditambahkan', 'active_elder':elder, 'feedback':feedback})
        else:
            return render(request, 'feedback.html', {'elders':elders, 'error':form.errors, 'active_elder':elder, 'feedback':feedback})
            
class FeedbackDetail(View):
    @classmethod
    def as_view(cls, **initkwargs):
        view = super(FeedbackDetail, cls).as_view(**initkwargs)
        return login_required(view, redirect_field_name=None)

    def get(self, request, id):
        cek_session(request)
        elder=None
        if request.session.get('active_elder') is not None and request.session['active_elder']!=0:
            elder=Elder.objects.get(pk=request.session.get('active_elder'))
        elders=Elder.get_cared_elder(user=CareGiver.objects.get(user=request.user))
        feedback=Feedback.objects.filter(owner=request.user, id=id)
        if feedback:
            return render(request, 'feedback_view.html', {'elders':elders, 'active_elder':elder, 'feedback':feedback[0]})
        return HttpResponseRedirect(reverse('notif_elder'))
        
    def post(self, request, id):
        cek_session(request)
        elder=None
        if request.session.get('active_elder') is not None and request.session['active_elder']!=0:
            elder=Elder.objects.get(pk=request.session.get('active_elder'))
        elders=Elder.get_cared_elder(user=CareGiver.objects.get(user=request.user))
        feedback=Feedback.objects.filter(owner=request.user, id=id)
        if feedback:
            form=ResponseForm(request.POST)
            if form.is_valid():
                new=form.save(commit=False)
                new.owner=request.user
                new.feedback=feedback[0]
                new.save()
                return render(request, 'feedback_view.html', {'elders':elders, 'success':'Respon berhasil ditambahkan', 'active_elder':elder, 'feedback':feedback[0]})
            return render(request, 'feedback_view.html', {'elders':elders, 'error':form.errors, 'active_elder':elder, 'feedback':feedback[0]})
        return HttpResponseRedirect(reverse('notif_elder'))