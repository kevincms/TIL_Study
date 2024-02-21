import discord

TOKEN = '<TOKEN>'
# Whitelist Gateway Intent 제도로 인한 봇 권한 문제로 추정. 디스코드 특정버전부터 이 코드가 들어가기 시작한 것 같음.
# Privileged Gateway Intents 설정에서 권한을 설정할 수 있음.
intents = discord.Intents.default()

# 봇 객체 생성
client=discord.Client(intents=intents)

client.run(TOKEN)