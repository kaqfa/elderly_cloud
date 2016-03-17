
from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
# from django.http import HttpResponse

from rest_framework.routers import DefaultRouter
# from django.views.generic import TemplateView

from base.views import Login
from member.views import Elders, Signup, CareGivers
from tracker.views import Trackers

router = DefaultRouter()
router.register(r'members', Signup, 'Signup')
router.register(r'login', Login, 'Login')
router.register(r'elders', Elders, 'Elders')
router.register(r'caregivers', CareGivers, 'Caregivers')
router.register(r'trackers', Trackers, 'Trackers')

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^summernote/', include('django_summernote.urls')),
    url(r'^api/', include(router.urls)),

    url(r'^webapp/', include('base.urls')),
    url(r'^$', 'base.views.frontend', name='frontend'),
    # in case of development uncomment below lines and http import
    # url(r'^robots.txt$', lambda r: HttpResponse(
    #     "User-agent: *\nDisallow: /", mimetype="text/plain")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
