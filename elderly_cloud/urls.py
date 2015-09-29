"""elderly_cloud URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
	https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
	1. Add an import:  from my_app import views
	2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
	1. Add an import:  from other_app.views import Home
	2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
	1. Add an import:  from blog import urls as blog_urls
	2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin

from django.conf import settings
from django.conf.urls.static import static
from base.views import load_page, user_auth, status, user_logout, caregiver_auth_token, elder_auth_token
from notification.views import notifs, hello
from contact.views import contacts
from elder_profile.views import diseases, medicalTreatments
from tracker.views import trackers
from info.views import infos
from member.views import elders, Signup
from rest_framework.authtoken.views import obtain_auth_token

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'notifs', notifs, 'Notification')
router.register(r'contacts', contacts, 'Contacts')
router.register(r'disease_hists', diseases, 'Diseases')
router.register(r'med_hists', medicalTreatments, 'Medical Treatments')
router.register(r'trackers', trackers, 'Trackers')
router.register(r'info', infos, 'Info')
router.register(r'elders', elders, 'Elders')
router.register(r'templates/hello', hello, 'Hello')
router.register(r'members', Signup, 'Signup')

urlpatterns = [
	url(r'^admin/', include(admin.site.urls)),
	url(r'^$', load_page),
	url(r'^login/', user_auth, name='login'),
	url(r'^status/', status, name='status'),
	url(r'^logout/', user_logout, name='logout'),
	url(r'^api/login/elder/', elder_auth_token),
	url(r'^api/login/', caregiver_auth_token),
	url(r'^api/', include(router.urls)),
	url(r'^page/(?P<page>\w+)/', load_page, name='load'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
