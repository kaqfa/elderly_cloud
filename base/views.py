from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse

"""
Authentication Start
"""
from rest_framework import parsers, renderers, serializers
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from member.models import CareGiver, Elder


class CareGiverAuthToken(APIView):
	throttle_classes = ()
	permission_classes = ()
	parser_classes = (parsers.FormParser, parsers.MultiPartParser, parsers.JSONParser,)
	renderer_classes = (renderers.JSONRenderer,)
	serializer_class = AuthTokenSerializer

	def post(self, request):
		serializer = self.serializer_class(data=request.data)
		serializer.is_valid(raise_exception=True)
		user = serializer.validated_data['user']
		if CareGiver.objects.filter(user=user):
			token, created = Token.objects.get_or_create(user=user)
			return Response({'token': token.key})
		else:
			return  Response({'non_field_errors':["Unable to log in with provided credentials."]})

class ElderAuthToken(APIView):
	throttle_classes = ()
	permission_classes = ()
	parser_classes = (parsers.FormParser, parsers.MultiPartParser, parsers.JSONParser,)
	renderer_classes = (renderers.JSONRenderer,)

	def post(self, request):
		if request.data.get('code') is None or request.data.get('code') == '':
			return Response({'code':["This field is required."]})
		else:
			code = request.data.get('code')
			elder = Elder.objects.filter(code=code)
			if elder:
				elder = elder[0]
				token, created = Token.objects.get_or_create(user=elder.user)
				return Response({'token': token.key})
			else:
				return Response({'non_field_errors':['Unable to log in with provided credentials.']})

caregiver_auth_token = CareGiverAuthToken.as_view()
elder_auth_token = ElderAuthToken.as_view()
"""
Authentication End
"""

def load_page(request, page=None):
	if page == None:
		return render(request, 'index.html')

	return render(request, page + '.html')


def user_auth(request):
	user = authenticate(username='coba', password='lel')
	login(request, user)
	return HttpResponseRedirect(reverse('status'))


def user_logout(request):
	logout(request)
	return HttpResponseRedirect(reverse('status'))


def status(request):
	if request.user.is_authenticated():
		return HttpResponse("Logged in")
	else:
		return HttpResponse("Logged out")