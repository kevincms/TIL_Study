import requests
import requests
from requests.api import request
url="https://www.google.co.kr/"
count=1

response=requests.get(url)
response.raise_for_status()

print("%d. %d"%(count,response.status_code)) # 1. 응답코드
count+=1

print("%d. %d"%(count,requests.codes.ok))
count+=1

print("%d. %s"%(count,response.json))
count+=1