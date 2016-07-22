from rest_framework import viewsets, mixins
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.decorators import list_route
from article.serializers import ArticleSerializer
from article.models import Article
from django.shortcuts import render

# Create your views here.

class Articles(mixins.ListModelMixin,
             viewsets.GenericViewSet):
    serializer_class = ArticleSerializer
    permission_classes = (IsAuthenticated,)
    queryset = Article.objects.all().order_by("-created")