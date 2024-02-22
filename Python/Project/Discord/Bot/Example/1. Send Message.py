import discord
 
TOKEN = '<TOKEN>'
CHANNEL_ID = '<CHANNEL ID>'
 
 
class MyClient(discord.Client):
    # 봇이 준비되었을 때 실행하는 함수
    async def on_ready(self):
        channel = self.get_channel(int(CHANNEL_ID))
        await channel.send('Hello World') # 원하는 채널에 메세지 보내기
 
 
intents = discord.Intents.default()
intents.message_content = True
client = MyClient(intents=intents)
client.run(TOKEN)