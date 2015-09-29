from rest_framework import viewsets, filters
from member.models import Elder, CareGiver, Member
from member.serializers import ElderSerializer, SignupSerializer, CareGiverSerializer
from rest_framework.parsers import JSONParser, FormParser, MultiPartParser
from rest_framework.response import Response
from rest_framework.permissions import AllowAny

# Create your views here.

class elders(viewsets.ReadOnlyModelViewSet):
	queryset = Elder.objects.all()
	serializer_class = ElderSerializer
	
class Signup(viewsets.GenericViewSet):
	queryset = Member.objects.all()
	serializer_class = SignupSerializer
	permission_classes = (AllowAny,)
	def create(self, request):
		serializer = SignupSerializer(data=request.data)
		if serializer.is_valid():
			signupData = serializer.save()
			if type(signupData) is Elder:
				serializer = ElderSerializer(signupData)
			elif type(signupData) is CareGiver:
				serializer = CareGiverSerializer(signupData)
			else:
				return Response(serializer.errors, status=400)
			return Response(serializer.data, status=201)
		return Response(serializer.errors, status=400)