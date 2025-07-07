from django.contrib import admin
from .models import ChatRoom, Message

# Register your models here.
@admin.register(ChatRoom)
class ChatRoomAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'created_at')
    search_fields = ('name',)
    list_filter = ('created_at',)
    
    
@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('id','user','chat_room', 'content','timestamp',)
    search_fields = ('text',)
    list_filter = ('timestamp', 'chat_room')