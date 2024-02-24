import discord
from datetime import datetime
 
TOKEN = '<TOKEN>'
CHANNEL_ID = '<CHANNEL_ID>'
 
 
class MyClient(discord.Client):
    # 봇이 준비되었을 때 실행하는 함수
    async def on_ready(self):
        ### 봇 이름
        print(f'Logged on as {self.user}!')
        ### 봇 상태 변경
        await self.change_presence(status=discord.Status.online)
    
    # 디스코드 채널 채널에 메세지가 올라올 경우 실행되는 함수
    async def on_message(self, message):
        # 아직 모름
        if message.author == self.user:
            return
        # 메세지의의 종류에 따라 메세지 전송
        if message.content == 'ping':
            await message.channel.send(f'pong {message.author.mention}')
        else:
            answer = self.get_answer(message.content)
            await message.channel.send(answer)
 
    def get_day_of_week(self):
        weekday_list = ['월요일', '화요일', '수요일', '목요일', '금요일', '토요일', '일요일']

        weekday = weekday_list[datetime.today().weekday()]
        date = datetime.today().strftime("%Y년 %m월 %d일")
        result = f'{date}({weekday})'
        return result
 
    def get_time(self):
        return datetime.today().strftime("%H시 %M분 %S초")
 
    def get_answer(self, text):
        trim_text = text.replace(" ", "")
 
        answer_dict = {
            '안녕': '안녕하세요. MyBot입니다.',
            '요일': ':calendar: 오늘은 {}입니다'.format(self.get_day_of_week()),
            '시간': ':clock9: 현재 시간은 {}입니다.'.format(self.get_time()),
        }
 
        if trim_text == '' or None:
            return "알 수 없는 질의입니다. 답변을 드릴 수 없습니다."
        elif trim_text in answer_dict.keys():
            return answer_dict[trim_text]
 
        return text + "은(는) 없는 질문입니다."
    
intents = discord.Intents.default()
intents.message_content = True
client = MyClient(intents=intents)
client.run(TOKEN)