import json
from channels.generic.websocket import AsyncWebsocketConsumer


class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        """客户端连接时"""
        # self.user = self.scope["user"]
        # print(self.user) # admin
        # print(self.channel_name) # specific.29a4ea4f99064ede8edc3305d7050ff5!59a6ebecae0b4873af0af625566d5c9c

        # 从url中获取参数
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = f'chat_{self.room_name}'

        # 加入房间组
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        # 接受 WebSocket 连接
        await self.accept()

    async def disconnect(self, close_code):
        # 离开房间组
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']

        # 向发送者回复消息
        # await self.send(text_data=json.dumps({
        #     'message': message
        # }))

        # 向房间组发送消息
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message
            }
        )

    # 接收来自房间组的消息
    async def chat_message(self, event):
        message = event['message']

        # 向 WebSocket 发送消息
        await self.send(text_data=json.dumps({
            'message': message
        }))
