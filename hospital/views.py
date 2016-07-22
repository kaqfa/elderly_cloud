from rest_framework import viewsets, mixins
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.decorators import list_route
from hospital.serializers import HospitalSerializer
from hospital.models import Hospital
from django.shortcuts import render

# Create your views here.

class Hospitals(mixins.ListModelMixin,
             viewsets.GenericViewSet):
    serializer_class = HospitalSerializer
    permission_classes = (IsAuthenticated,)
    queryset = Hospital.objects.all().order_by("-id")