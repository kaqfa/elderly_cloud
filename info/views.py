from rest_framework import viewsets

from info.models import Posting
from info.serializers import PostingSerializer


# Create your views here.

class infos(viewsets.ReadOnlyModelViewSet):
    queryset = Posting.objects.all()
    serializer_class = PostingSerializer