from django.db import models

from django.conf import settings

# Create your models here.


class ChatRoom(models.Model):
    name = models.CharField(max_length=255, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
    
class Message(models.Model):
    user = models.TextField(("User"), default="Anonymous")
    chat_room = models.ForeignKey(ChatRoom, on_delete=models.CASCADE, related_name='messages')
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.user}: {self.content} at {self.timestamp.strftime('%I:%M %p')}"  
