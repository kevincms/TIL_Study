import discord
 
TOKEN = '<TOKEN>'
CHANNEL_ID = '<CHANNEL ID>'
 
 
class MyClient(discord.Client):
    # 봇이 준비되었을 때 실행하는 함수
    async def on_ready(self):
        # 봇 이름
        print(f'Logged on as {self.user}!')
        # 봇 상태변경
        await self.change_presence(status=discord.Status.online, activity=discord.Game("대기중"))
 
 
intents = discord.Intents.default()
intents.message_content = True
client = MyClient(intents=intents)
client.run(TOKEN)