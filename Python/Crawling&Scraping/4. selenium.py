# import selenium
import os
from selenium import webdriver

folder_path=os.path.dirname(__file__)
chromedriver="/chromedriver.exe"
chromedriver_path=folder_path+chromedriver

browser=webdriver.Chrome(chromedriver_path)

url="https://www.naver.com/"
browser.get(url)
# chromedriver.implicitly_wait(10)