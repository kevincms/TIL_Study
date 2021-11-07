import os
import time
from selenium import webdriver

folder_path=os.path.dirname(__file__)
chromedriver="/chromedriver.exe"
chromedriver_path=folder_path+chromedriver

browser=webdriver.Chrome(chromedriver_path) # 브라우저 실행

url="https://www.naver.com/"
browser.get(url) # 링크로 이동



time.sleep(10) # .py 파일의 경우 프로그램이 종료되면 브라우저가 자동종료됨 (.ipynb 사용권장)