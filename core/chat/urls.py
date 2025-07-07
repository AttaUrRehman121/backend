from django.urls import path
from .views import ChatRoomListCreateAPIView, MessageListView

urlpatterns = [
    path("rooms/", ChatRoomListCreateAPIView.as_view(), name="chatroom-list-create"),
    path("messages/<str:room_name>/", MessageListView.as_view(), name="message-list"),
]
