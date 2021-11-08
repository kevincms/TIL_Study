import os
import requests
import bs4

folder_path=os.path.dirname(__file__)
url="https://www.acmicpc.net/step"
baekjoon_url="https://www.acmicpc.net/"

response=requests.get(url)
response.raise_for_status()
soup=bs4.BeautifulSoup(response.text,"lxml")

file_name="/test.txt"
create_file=folder_path+file_name

tr_list=soup.find("tbody").find_all("tr")
dir_name=tr_list[0].td.get_text()
dir_name=dir_name+"_"+tr_list[0].td.find_next_sibling("td").get_text()
# print(dir_name)

problem_url=baekjoon_url+tr_list[0].td.find_next_sibling("td").a["href"]
# print(problem_url)

response=requests.get(problem_url)
response.raise_for_status()
soup=bs4.BeautifulSoup(response.text,"lxml")

problem_tr_list=soup.find("tbody").find_all("tr")
# print(problem_tr_list) # 리스트가 문제 수 의 2배로 되어 있음. 문제사이 텍스트가 추가되어 있음.



# # for i in range(12):
    