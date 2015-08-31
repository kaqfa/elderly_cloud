from django.db import models
from django.contrib.auth.models import User


class Elder(models.Model):
	code = models.CharField(max_length=8, blank=False, null=False)
	name = models.CharField(max_length=100, blank=False, null=False, default='')
	cared_by = models.ManyToManyField(User, through='Caregiving')
	
	@staticmethod
	def get_cared_elder(user):
		return Elder.objects.filter(cared_by__in=user)
		
	def get_kondisi():
		return self.dailycondition_set
		
	def get_kondisi_terakhir():
		return self.dailycondition_set.latest('id')
	
	def count_perawat():
		return self.cared_by.count()
		
	def get_riwayat_penyakit():
		return self.diseasehist_set
		
	def get_perawatan_medis():
		return self.medicaltreatmenthist_set
		
	def get_note():
		return self.note_set


class Caregiving(models.Model):
	user = models.ForeignKey(User)
	elder = models.ForeignKey(Elder)


class AdminInvitation(models.Model):
	user = models.ForeignKey(User)
	email_to_invite = models.CharField(max_length=45)
	status = models.CharField(max_length=1)
