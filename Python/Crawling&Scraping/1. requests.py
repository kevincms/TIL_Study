import os
import requests

foler_path=os.path.dirname(__file__)
file_name="\\test_google.html"
create_file=foler_path+file_name
url="https://www.google.co.kr/"
count=1

response=requests.get(url)
response.raise_for_status() # 2. 응답여부 확인 (if 문과 달리 오류를 발생시킴)

# 1. 응답코드 200-정상
print("%d. %d"%(count,response.status_code)) 
count+=1

# 2. 응답여부 확인
if response.status_code==requests.codes.ok:
    print("{}. 접근가능".format(count))
else:
    print("{}. 접근불가능 [에러코드 {}]".format(count,response.status_code))
count+=1

# User-Agent 응답여부
headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36"}
response=requests.get(url,headers=headers)
response.raise_for_status()

with open(create_file,"w",encoding="utf8") as google:
    google.write(response.text)
