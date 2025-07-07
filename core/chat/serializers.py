from rest_framework import serializers
from .models import ChatRoom, Message
class ChatRoomSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = ChatRoom
        fields = ['id', 'name']
        

class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ['id', 'user', 'chat_room', 'content', 'timestamp']