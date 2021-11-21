import os
import requests
import bs4

folder_path=os.path.dirname(__file__)
url="https://www.acmicpc.net/step"
baekjoon_url="https://www.acmicpc.net/"

response=requests.get(url)
response.raise_for_status()
soup=bs4.BeautifulSoup(response.text,"lxml")

file_name="\\test.html"
create_file=folder_path+file_name

step_problem_num=2 # 가져올 스탭 문제 번호
step_problem_num=step_problem_num-1
tr_list=soup.find("tbody").find_all("tr")
dir_name=tr_list[step_problem_num].td.get_text()
dir_name=dir_name+"_"+tr_list[step_problem_num].td.find_next_sibling("td").get_text()
# print(len(tr_list))

problem_url=baekjoon_url+tr_list[step_problem_num].td.find_next_sibling("td").a["href"]
# print(problem_url)

response=requests.get(problem_url)
response.raise_for_status()
soup=bs4.BeautifulSoup(response.text,"lxml")

problem_tr_list=soup.find("tbody").find_all("tr")
# print(len(problem_tr_list)) # 리스트가 문제 수 의 2배로 되어 있음. 문제사이 텍스트가 추가되어 있음.

wanted_problem_num=4 # 가져올 문제 번호
wanted_problem_num=(wanted_problem_num-1)*2
problem_num=problem_tr_list[wanted_problem_num].find("td").get_text()
problem_title=problem_tr_list[wanted_problem_num].find("td").find_next_sibling("td").find_next_sibling("td").get_text()
problem_file_name=problem_num+". "+problem_title
# print(problem_file_name)

down_url=baekjoon_url+problem_tr_list[wanted_problem_num].find("a")["href"]
response=requests.get(down_url)
response.raise_for_status()

soup=bs4.BeautifulSoup(response.text,"lxml")
image=soup.find("div",attrs={"id":"problem-body"}).find_all("img")
if image:        
    for i in range(len(image)):
        file_name="\\image{}.png".format(i+1)
        image[i]=image[i]["src"]
        if not ("https" in image[i]):
            image[i]=baekjoon_url+image[i]
        test_image_response=requests.get(image[i])
        test_image_response.raise_for_status()
        create_file=folder_path+file_name
        with open(create_file,"wb") as test_picture:
            test_picture.write(test_image_response.content) #  사진을 가져옴 
        image_modify_url=folder_path+file_name
        file_name="\\test.html"
        create_file=folder_path+file_name
        soup.find("div",attrs={"id":"problem-body"}).find_all("img")[i]["src"]=image_modify_url
        with open(create_file,"w",encoding="utf-8") as down_html:
            down_html.write(str(soup)) # 사진 url 수정 html
else:
    with open(create_file,"w",encoding="utf-8") as down_html:
        down_html.write(response.text) # html


problem_body_list=soup.find("div",attrs={"id":"problem-body"}).find_all("div",attrs={"class":"col-md-12"})
problem_body_text="\'\'\'\n"
for i in range(3):
    problem_body_text=problem_body_text+problem_body_list[i].find("h2").get_text()+"\n -"
    problem_body_text=problem_body_text+problem_body_list[i].find("div",attrs={"class":"problem-text"}).get_text().strip()+"\n"
for i in range(4,len(problem_body_list)-1):
    temp_list=problem_body_list[i].find_all("div",attrs={"class":"col-md-6"})
    for j in range(len(temp_list)):
        problem_body_text=problem_body_text+temp_list[j].find("h2").get_text().replace("복사","").strip()+"\n -"
        if not temp_list[j].find("pre").get_text():
            problem_body_text=problem_body_text+"없음\n"
        else:
            problem_body_text=problem_body_text+temp_list[j].find("pre").get_text()+"\n"

problem_body_text=problem_body_text+"\'\'\'"
file_name="\\test.py"
create_file=folder_path+file_name
with open(create_file,"w",encoding="utf-8") as problem_python:
    problem_python.write(problem_body_text)