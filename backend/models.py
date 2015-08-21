from django.db import models

# Create your models here.
class User(models.Model):
	username = models.CharField(max_length=45, blank=False, default='')
	
class Elder(models.Model):
	code = models.CharField(max_length=45, blank=False, default='')
	name = models.CharField(max_length=45, blank=False, default='')
	
class Tracker_template(models.Model):
	name = models.CharField(max_length=45, blank=False, default='')
	field1 = models.CharField(max_length=45)
	field2 = models.CharField(max_length=45)
	field3 = models.CharField(max_length=45)
	field4 = models.CharField(max_length=45)
	field5 = models.CharField(max_length=45)
	
class Tracker(models.Model):
	name = models.CharField(max_length=45, blank=False, default='')
	field1 = models.CharField(max_length=45)
	field2 = models.CharField(max_length=45)
	field3 = models.CharField(max_length=45)
	field4 = models.CharField(max_length=45)
	field5 = models.CharField(max_length=45)

class Point_of_interest(models.Model):
	name = models.CharField(max_length=45)
	category = models.CharField(max_length=45)
	address = models.CharField(max_length=45)
	lattitude = models.CharField(max_length=45)
	longitude = models.CharField(max_length=45)
	
class Notif_template(models.Model):
	name = models.CharField(max_length=45)
	
class Admin_invitation(models.Model):
	user_id = models.ForeignKey(User)
	email_to_invite = models.CharField(max_length=45)
	status = models.CharField(max_length=1)
	
class Posting(models.Model):
	user_id = models.ForeignKey(User)
	title = models.CharField(max_length=45)
	content = models.TextField()
	category = models.CharField(max_length=45)
	
class Feedback(models.Model):
	user_id = models.ForeignKey(User)
	feedback = models.CharField(max_length=45)

class Disease_hist(models.Model):
	elder_id = models.ForeignKey(Elder)
	disease = models.CharField(max_length=45)
	
class Medications(models.Model):
	elder_id = models.ForeignKey(Elder)
	name = models.CharField(max_length=45)
	dosage = models.CharField(max_length=45)
	
class Medical_treatment_hist(models.Model):
	elder_id = models.ForeignKey(Elder)
	treatment = models.TextField()
	
class Daily_condition(models.Model):
	elder_id = models.ForeignKey(Elder)
	condition = models.CharField(max_length=45)
	time_record = models.DateTimeField()
	
class Emergency_call(models.Model):
	elder_id = models.ForeignKey(Elder)
	emergancy_time = models.DateTimeField()
	
class Notifications(models.Model):
	elder_id = models.ForeignKey(Elder)
	notif = models.CharField(max_length=45)

class Log_tracker(models.Model):
	elder_id = models.ForeignKey(Elder)
	tracker_id = models.ForeignKey(Tracker)
	value1 = models.IntegerField(default=0)
	value2 = models.IntegerField(default=0)
	value3 = models.IntegerField(default=0)
	value4 = models.IntegerField(default=0)
	value5 = models.IntegerField(default=0)
	
class Caregiving(models.Model):
	user_id = models.ForeignKey(User)
	elder_id = models.ForeignKey(Elder)
	
class Note(models.Model):
	user_id = models.ForeignKey(User)
	elder_id = models.ForeignKey(Elder)
	title = models.CharField(max_length=45)
	
class Respond_emergency_call(models.Model):
	user_id = models.ForeignKey(User)
	emergency_call_id = models.ForeignKey(Emergency_call)