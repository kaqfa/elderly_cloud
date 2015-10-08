from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

from base.views import Login
from notification.views import Hello
from rest_framework.routers import DefaultRouter
from base.views import load_page, user_auth, status, user_logout
from notification.views import Notifs
from django.views.generic import TemplateView

from contact.views import contacts
from elder_profile.views import Diseases, MedicalTreatments
from tracker.views import Trackers
from info.views import infos
from member.views import Elders, Signup


router = DefaultRouter()
router.register(r'notifs', Notifs, 'Notification')
router.register(r'contacts', contacts, 'Contacts')
router.register(r'disease_hists', Diseases, 'Diseases')
router.register(r'med_hists', MedicalTreatments, 'Medical Treatments')
router.register(r'trackers', Trackers, 'Trackers')
router.register(r'info', infos, 'Info')
router.register(r'elders', Elders, 'Elders')
router.register(r'templates/hello', Hello, 'Hello')
router.register(r'members', Signup, 'Signup')
router.register(r'login', Login, 'Login')

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/', include(router.urls)),
    url(r'^login/', user_auth, name='login'),
	url(r'^logout/', user_logout, name='logout'),
	url(r'^status/', status, name='status'),
    url(r'^(?P<page>[\w]*)/$', load_page.as_view(), name='load'),
    url(r'^summernote/', include('django_summernote.urls')),
    url(r'^$', load_page.as_view(), name='index'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)