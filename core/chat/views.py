from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import ChatRoom, Message
from .serializers import ChatRoomSerializer, MessageSerializer

class ChatRoomListCreateAPIView(generics.ListCreateAPIView):
 
    queryset = ChatRoom.objects.all()
    serializer_class = ChatRoomSerializer

    def perform_create(self, serializer):
        serializer.save()



class MessageListView(APIView):
    def get(self, request, room_name):
        try:
            room = ChatRoom.objects.get(name=room_name)
        except ChatRoom.DoesNotExist:
            return Response({"error": "Chat room not found"}, status=status.HTTP_404_NOT_FOUND)

        messages = Message.objects.filter(chat_room=room).order_by('timestamp')
        serializer = MessageSerializer(messages, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)