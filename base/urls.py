from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static

# from notification.views import Hello

from base.views import status, user_logout, Index
# from notification.views import Notifs, NotifikasiElder
# DetailNotifikasiElder, EditNotifikasiElder, HapusNotifikasiElder
# NotifikasiCG, DetailNotifikasiCG, ResponNotifikasi
# from django.views.generic import TemplateView

# from contact.views import contacts, ContactTable, ContactDetail
# ContactEdit, ContactDelete
# from elder_profile.views import Diseases, MedicalTreatments, MTTable
# MTDetail, MTEdit, MTDelete, DHTable, DHDetail, DHEdit, DHDelete, NoteTable
# NoteDetail, NoteEdit, NoteDelete
# from tracker.views import Trackers, KondisiHarian, DetakJantung, GulaDarah
# from info.views import infos, InfoAll, TipsAll, PostDetail, POIList
from member.views import Parents, UpdateElder, DeleteElder
from member.views import set_active_elder, UpdateProfile
# from feedback.views import FeedbackList, FeedbackDetail
# from partner.views import UpdateAvailability, AgendaTable, AgendaEdit
# from partner.views import AgendaDetail, AgendaDelete, RoomTable, RoomEdit
# RoomDetail, RoomDelete, RoomClassTable, RoomClassEdit, RoomClassDetail
# from partner.views import RoomClassDelete

urlpatterns = [
    url(r'^$', Index.as_view(), name='index'),
    url(r'^logout/', user_logout, name='logout'),
    url(r'^status/', status, name='status'),
    url(r'^parents/$', Parents.as_view(), name='parents'),
    url(r'^parents/(?P<id>[0-9]*)/edit/$',
        UpdateElder.as_view(), name='parents_edit'),
    url(r'^parents/(?P<id>[0-9]*)/delete/$',
        DeleteElder.as_view(), name='parents_del'),
    # url(r'^notification/elder/$',
    # NotifikasiElder.as_view(), name='notif_elder'),
    # url(r'^notification/elder/(?P<id>[0-9]*)/$',
    # DetailNotifikasiElder.as_view(), name='dt_notif_elder'),
    # url(r'^notification/elder/(?P<id>[0-9]*)/edit/$',
    # EditNotifikasiElder.as_view(), name='edit_notif_elder'),
    # url(r'^notification/elder/(?P<id>[0-9]*)/delete/$',
    # HapusNotifikasiElder.as_view(), name='del_notif_elder'),
    # url(r'^notification/$', NotifikasiCG.as_view(), name='notif_cg'),
    # url(r'^notification/(?P<id>[0-9]*)/$',
    # DetailNotifikasiCG.as_view(), name='dt_notif_cg'),
    # url(r'^notification/(?P<id>[0-9]*)/respon/$',
    # ResponNotifikasi.as_view(), name='respon_notif'),
    # url(r'^treatment/$', MTTable.as_view(), name='treatment'),
    # url(r'^treatment/(?P<id>[0-9]*)/$',
    # MTDetail.as_view(), name='dt_treatment'),
    # url(r'^treatment/(?P<id>[0-9]*)/edit/$',
    # MTEdit.as_view(), name='edit_treatment'),
    # url(r'^treatment/(?P<id>[0-9]*)/delete/$',
    # MTDelete.as_view(), name='del_treatment'),
    # url(r'^disease/$', DHTable.as_view(), name='disease'),
    # url(r'^disease/(?P<id>[0-9]*)/$',
    # DHDetail.as_view(), name='dt_disease'),
    # url(r'^disease/(?P<id>[0-9]*)/edit/$',
    # DHEdit.as_view(), name='edit_disease'),
    # url(r'^disease/(?P<id>[0-9]*)/delete/$',
    # DHDelete.as_view(), name='del_disease'),
    # url(r'^note/$', NoteTable.as_view(), name='note'),
    # url(r'^note/(?P<id>[0-9]*)/$', NoteDetail.as_view(), name='dt_note'),
    # url(r'^note/(?P<id>[0-9]*)/edit/$',
    # NoteEdit.as_view(), name='edit_note'),
    # url(r'^note/(?P<id>[0-9]*)/delete/$',
    # NoteDelete.as_view(), name='del_note'),
    # url(r'^contact/$', ContactTable.as_view(), name='contact'),
    # url(r'^contact/(?P<id>[0-9]*)/$',
    # ContactDetail.as_view(), name='dt_contact'),
    # url(r'^contact/(?P<id>[0-9]*)/edit/$',
    # ContactEdit.as_view(), name='edit_contact'),
    # url(r'^contact/(?P<id>[0-9]*)/delete/$',
    # ContactDelete.as_view(), name='del_contact'),
    # url(r'^history/daily/$', KondisiHarian.as_view(), name='kondisi_harian'),
    # url(r'^history/heartrate/$',
    # DetakJantung.as_view(), name='detak_jantung'),
    # url(r'^history/glucose/$', GulaDarah.as_view(), name='gula_darah'),
    # url(r'^info/$', InfoAll.as_view(), name='info'),
    # url(r'^tips/$', TipsAll.as_view(), name='tips'),
    # url(r'^location/$', POIList.as_view(), name='location'),
    # url(r'^(?P<type>info|tips)/(?P<id>[0-9]*)/$',
    # PostDetail.as_view(), name='post'),
    # url(r'^feedback/$', FeedbackList.as_view(), name='feedback'),
    # url(r'^feedback/(?P<id>[0-9]*)/$',
    # FeedbackDetail.as_view(), name='feedback_detail'),
    url(r'^profile/$', UpdateProfile.as_view(), name='profile'),
    url(r'^activate/(?P<id>[0-9]*)/', set_active_elder, name='set_elder'),
    # url(r'^availability/$',
    # UpdateAvailability.as_view(), name='availability'),
    # url(r'^agenda/$', AgendaTable.as_view(), name='agenda'),
    # url(r'^agenda/(?P<id>[0-9]*)/$',
    # AgendaDetail.as_view(), name='dt_agenda'),
    # url(r'^agenda/(?P<id>[0-9]*)/edit/$',
    # AgendaEdit.as_view(), name='edit_agenda'),
    # url(r'^agenda/(?P<id>[0-9]*)/delete/$',
    # AgendaDelete.as_view(), name='del_agenda'),
    # url(r'^room/class/$', RoomClassTable.as_view(), name='rclass'),
    # url(r'^room/class/(?P<id>[0-9]*)/$',
    # RoomClassDetail.as_view(), name='dt_rclass'),
    # url(r'^room/class/(?P<id>[0-9]*)/edit/$',
    # RoomClassEdit.as_view(), name='edit_rclass'),
    # url(r'^room/class/(?P<id>[0-9]*)/delete/$',
    # RoomClassDelete.as_view(), name='del_rclass'),
    # url(r'^room/$', RoomTable.as_view(), name='room'),
    # url(r'^room/(?P<id>[0-9]*)/$', RoomDetail.as_view(), name='dt_room'),
    # url(r'^room/(?P<id>[0-9]*)/edit/$',
    # RoomEdit.as_view(), name='edit_room'),
    # url(r'^room/(?P<id>[0-9]*)/delete/$',
    # RoomDelete.as_view(), name='del_room'),
    url(r'^(?P<page>[\w]*)/$', Index.as_view(), name='load'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
