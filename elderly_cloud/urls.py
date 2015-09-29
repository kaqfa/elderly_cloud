from django.conf.urls import include, url
from django.contrib import admin

from django.conf import settings
from django.conf.urls.static import static

from base.views import load_page, user_auth, status, user_logout
from notification.views import notifs
from contact.views import contacts
from elder_profile.views import diseases, medicalTreatments
from tracker.views import trackers
from info.views import infos

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'notifs', notifs, 'Notification')
router.register(r'contacts', contacts, 'Contacts')
router.register(r'disease_hists', diseases, 'Diseases')
router.register(r'med_hists', medicalTreatments, 'Medical Treatments')
router.register(r'trackers', trackers, 'Trackers')
router.register(r'info', infos, 'Info')

urlpatterns = [
                  url(r'$/', load_page, name='index'),
                  url(r'^admin/', include(admin.site.urls)),
                  url(r'^(?P<page>[\w]*)/$', load_page, name='load'),
                  url(r'^login/', user_auth, name='login'),
                  url(r'^status/', status, name='status'),
                  url(r'^logout/', user_logout, name='logout'),
                  url(r'^api/', include(router.urls)),
                  url(r'^summernote/', include('django_summernote.urls')),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
