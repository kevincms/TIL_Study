import discord

TOKEN = '<TOKEN>'

# Whitelist Gateway Intent 제도 관련 권한
intents = discord.Intents.default()
intents.message_content = True # 메세지를 읽는 권한 True로 변경

# 객체 생성
client = discord.Client(intents=intents)

key_command="!안녕"
command_dict={key_command:"안녕하세요!"}

# discord 데코레이터
@client.event
# on_message : discord에서 제공하는 함수. 채팅채널에 매세지 생성시 실행됨,
# message : discord.message의 객채. 이 객체를 통해 메세지에 접근 할 수있다.
async def on_message(message):
    # message 읽어오기
    if message.content == key_command:
        # message.channel : 메세지 채널 불러오기
        # Channel.send : 매새지 전송
        await message.channel.send(command_dict[key_command])

client.run(TOKEN)