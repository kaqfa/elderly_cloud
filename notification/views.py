from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from notification.models import Notifications
from notification.serializers import NotificationsSerializer


@api_view(['GET', 'POST'])
def notif_list(request):
    """
    List all notification, or create a new notification.
    """
    if request.method == 'GET':
        notif = Notifications.objects.all()
        serializer = NotificationsSerializer(notif, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = NotificationsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Create your views here.
