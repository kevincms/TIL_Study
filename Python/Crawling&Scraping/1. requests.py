import os
import requests

folder_path=os.path.dirname(__file__)
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

# User-Agent String User-Agent가 존재하지 않을 때 연결이 되지 않는 경우가 다수 존재)
user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36 Edg/95.0.1020.40"
headers={"User-Agent":user_agent}
test_image_url="https://www.google.co.kr/images/branding/googlelogo/1x/googlelogo_light_color_272x92dp.png"
test_image_response=requests.get(test_image_url,headers=headers)
test_image_response.raise_for_status()

file_name="/test.html"
create_file=folder_path+file_name
with open(create_file,"w") as test_html:
    test_html.write(response.text) #  html 코드를 가져옴

file_name="/test_image.png"
create_file=folder_path+file_name

with open(create_file,"wb") as test_picture:
    test_picture.write(test_image_response.content) #  사진을 가져옴
