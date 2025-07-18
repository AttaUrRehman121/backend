import json
from channels.generic.websocket import AsyncWebsocketConsumer
from .models import Message, ChatRoom
from asgiref.sync import sync_to_async

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = f'chat_{self.room_name}'

        # Create room if not exists
        await self.get_or_create_room()

        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    async def receive(self, text_data):
        data = json.loads(text_data)
        message = data["message"]
        username = data.get("username")
        timestamp = data.get("timestamp", "")

        
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                "type": "chat_message",
                "message": message,
                "username": username,
                "timestamp": timestamp
            }
        )

       
        await self.save_message(username, message, timestamp)

    async def chat_message(self, event):
        await self.send(text_data=json.dumps({
            "message": event["message"],
            "username": event["username"],
            "timestamp": event["timestamp"]
        }))

    @sync_to_async
    def get_or_create_room(self):
        self.chat_room, _ = ChatRoom.objects.get_or_create(name=self.room_name)

    @sync_to_async
    def save_message(self, username, message, timestamp):
        Message.objects.create(
            user=username,
            chat_room=self.chat_room,
            content=message,
            timestamp=timestamp
        )
