from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from member.models import Elder, CareGiver, CareGiving
from django.contrib.auth.models import User
from django.utils.crypto import get_random_string
from django.contrib.auth.models import Group
from rest_framework.authtoken.serializers import AuthTokenSerializer

class LoginSerializer(AuthTokenSerializer):
	code = serializers.CharField(required=False)