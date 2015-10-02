from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.permissions import AllowAny

from member.models import Elder, CareGiver, Member
from member.serializers import ElderSerializer, SignupSerializer, CareGiverSerializer


class Elders(viewsets.ReadOnlyModelViewSet):
    queryset = Elder.objects.all()
    serializer_class = ElderSerializer


class Signup(viewsets.GenericViewSet):
    queryset = Member.objects.all()
    serializer_class = SignupSerializer
    permission_classes = (AllowAny,)

    def create(self, request):
        serializer = SignupSerializer(data=request.data)
        if serializer.is_valid():
            signup_data = serializer.save()
            if type(signup_data) is Elder:
                serializer = ElderSerializer(signup_data)
            elif type(signup_data) is CareGiver:
                serializer = CareGiverSerializer(signup_data)
            else:
                return Response(serializer.errors, status=400)
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
