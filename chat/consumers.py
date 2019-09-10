from channels.generic.websocket import AsyncWebsocketConsumer
from channels.auth import login
import json

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = 'chat_%s' % self.room_name

        # Join room group
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name,

        )


        await self.accept()

    async def disconnect(self, close_code):
        # Leave room group
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name,

        )

    # Receive message from WebSocket
    async def receive(self, text_data):
        username_str = None #newly added
        username = self.scope["user"] #newly added
        username_str = username.username #newly added

        text_data_json = json.loads(text_data)
        message = text_data_json['message']

        # Send message to room group
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message,
                'username': username_str #newly added
            }
        )

    # Receive message from room group
    async def chat_message(self, event):
        message = event['message']
        username = event['username'] #newly added

        # Send message to WebSocket
        await self.send(text_data=json.dumps({
            'message': message,
            'username':username #newly added

        }))
