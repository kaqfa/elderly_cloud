
from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
# from django.http import HttpResponse

from rest_framework.routers import DefaultRouter
# from django.views.generic import TemplateView

from base.views import Login, redirect
from member.views import Elders, Signup, CareGivers, Profile
from article.views import Articles
from hospital.views import Hospitals
from tracker.views import Trackers

router = DefaultRouter()
router.register(r'members', Signup, 'Signup')
router.register(r'login', Login, 'Login')
router.register(r'elders', Elders, 'Elders')
router.register(r'caregivers', CareGivers, 'Caregivers')
router.register(r'trackers', Trackers, 'Trackers')
router.register(r'profile', Profile, 'Profile')
router.register(r'hospital', Hospitals, 'Hospitals')
router.register(r'article', Articles, 'Articles')

urlpatterns = [    
    url(r'^summernote/', include('django_summernote.urls')),
    url(r'^api/', include(router.urls)),
    url(r'^admin/', include(admin.site.urls)),

    url(r'^web/', include('base.urls')),
    url(r'^', redirect),
    # url(r'^$', 'base.views.frontend', name='frontend'),
    # in case of development uncomment below lines and http import
    # url(r'^robots.txt$', lambda r: HttpResponse(
    #     "User-agent: *\nDisallow: /", mimetype="text/plain")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
