import json
from channels.generic.websocket import AsyncWebsocketConsumer
from asgiref.sync import async_to_sync
from .models import Mychats, Rooms
from django.contrib.auth.models import User
import datetime
from channels.db import database_sync_to_async
from channels.layers import get_channel_layer


class MychatApp(AsyncWebsocketConsumer):

    async def connect(self):
        try:
            user = self.scope['user']
            if user.is_authenticated:
                await self.accept()
                await self.channel_layer.group_add(f"mychat_app_{user.username}", self.channel_name)
                print("connected")
            else:
                print("closed")
                # Handle unauthenticated users (e.g., close the connection)
                await self.close()
        except Exception as e:
            print(e)


    async def disconnect(self, close_code):
        pass

    async def receive(self, text_data):
        text_data = json.loads(text_data)
        uniqueid = await self.save_chat(text_data)
        print("i am  called receive",uniqueid,text_data)
        await self.channel_layer.group_send(
            f"mychat_app_{text_data['user']}",
            {
                'type': 'send.msg',
                'msg': text_data['msg'],
                'uniqueid': uniqueid
            }
        )

    async def send_uniqueid(self, event):
            uniqueid = event.get('uniqueid')
            await self.send(json.dumps({'uniqueid': uniqueid}))

    @database_sync_to_async
    def save_chat(self, text_data):
        frnd = User.objects.get(username=text_data['user'])
        mychats, created = Mychats.objects.get_or_create(
            me=self.scope['user'], frnd=frnd)
        if created:
            mychats.chats = {}

        timestamp = str(datetime.datetime.now())
        mychats.chats[timestamp +
                      "1"] = {'user': 'me', 'msg': text_data['msg']}
        mychats.save()

        try:
            room, roomquery = Rooms.objects.get_or_create(
                chat=mychats, username=self.scope['user'])
        except Exception as e:
            print(e)

        mychats, created = Mychats.objects.get_or_create(
            me=frnd, frnd=self.scope['user'])
        if created:
            mychats.chats = {}

        mychats.chats[timestamp +
                      "2"] = {'user': self.scope['user'].username, 'msg': text_data['msg']}
        mychats.save()

        try:
            room, roomquery = Rooms.objects.get_or_create(
                chat=mychats, username=text_data['user'])
        except Exception as e:
            print(e)
        # Return the uniqueid
        return room.uniqueid

    async def send_videonofication(self, event):
        await self.send(event['msg'])
    
    async def send_msg(self, event):
        msg = event['msg']
        uniqueid = event.get('uniqueid', None)
        data = {'msg': msg, 'uniqueid': uniqueid}
        await self.send(json.dumps(data))

    async def chat_message(self, event):
        print(event['message'])
        await self.send(json.dumps("Total Online :- " + str(event['message'])))
