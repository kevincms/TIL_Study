import os
import requests
import bs4

folder_path="D:\\Baekjoon_step_problem"
baekjoon_url="https://www.acmicpc.net/"

def createFolder(directory):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except OSError:
        print ('Error: Creating directory. ' +  directory)

def not_avaible_str_in_file(file_string):
    not_avaible_str_list=["\\","/",":","*","?","\"","<",">","|"]
    for i in not_avaible_str_list:
        if i in file_string:
            if i=="\\":
                file_string=file_string.replace(i,"＼")
            elif i=="/":
                file_string=file_string.replace(i,"÷")
                # file_string=file_string.replace(i,"／")
            elif i==":":
                file_string=file_string.replace(i,"：")
            elif i=="*":
                file_string=file_string.replace(i,"×")
                # file_string=file_string.replace(i,"＊")
            elif i=="?":
                file_string=file_string.replace(i,"？")
            elif i=="\"":
                file_string=file_string.replace(i,"＂")
            elif i=="<":
                file_string=file_string.replace(i,"＜")
            elif i==">":
                file_string=file_string.replace(i,"＞")
            elif i=="|":
                file_string=file_string.replace(i,"｜")
    return file_string

def html_image_down(soup,create_dir,problem_file_name):
    image=soup.find("div",attrs={"id":"problem-body"}).find_all("img")
    if image:
        # pass
        for k in range(len(image)):
            file_name="image{}.png".format(k+1)
            image[k]=image[k]["src"]
            if not ("https" in image[k]):
                image[k]=baekjoon_url+image[k]
            image_response=requests.get(image[k])
            image_response.raise_for_status()
            create_file=create_dir+"\\"+file_name
            with open(create_file,"wb") as test_picture:
                test_picture.write(image_response.content) #  사진을 가져옴 
            image_modify_url=file_name
            create_file=create_dir+"\\"+problem_file_name+".html"
            soup.find("div",attrs={"id":"problem-body"}).find_all("img")[k]["src"]=image_modify_url
            with open(create_file,"w",encoding="utf-8") as down_html:
                down_html.write(str(soup)) # 사진 url 수정 html
    else:
        create_file=create_dir+"\\"+problem_file_name+".html"
        with open(create_file,"w",encoding="utf-8") as down_html:
            down_html.write(response.text) # html

def problem_language_down(soup,down_url,create_dir,problem_file_name,language_list):
    problem_body_list=soup.find("div",attrs={"id":"problem-body"}).find_all("div",attrs={"class":"col-md-12"})
    problem_body_text=language_list[0]+"\n"
    if problem_body_list[1].find("h2").get_text()=="제한": # 예외처리
        problem_body_text=problem_body_text+problem_body_list[0].find("h2").get_text()+"\n -"
        problem_body_text=problem_body_text+problem_body_list[0].find("div",attrs={"class":"problem-text"}).get_text().strip()+"\n"
        problem_body_text=problem_body_text+down_url+"\n"
        problem_body_text=problem_body_text+language_list[1]
        create_file=create_dir+"\\"+problem_file_name+language_list[2]
        with open(create_file,"w",encoding="utf-8") as problem_python:
            problem_python.write(problem_body_text)
        return
    for k in range(3):
        problem_body_text=problem_body_text+problem_body_list[k].find("h2").get_text()+"\n -"
        problem_body_text=problem_body_text+problem_body_list[k].find("div",attrs={"class":"problem-text"}).get_text().strip()+"\n"
    for k in range(4,len(problem_body_list)-1):
        temp_list=problem_body_list[k].find_all("div",attrs={"class":"col-md-6"})
        for l in range(len(temp_list)):
            problem_body_text=problem_body_text+temp_list[l].find("h2").get_text().replace("복사","").strip()+"\n -"
            if not temp_list[l].find("pre").get_text():
                problem_body_text=problem_body_text+"없음\n"
            else:
                problem_body_text=problem_body_text+temp_list[l].find("pre").get_text()+"\n"
    problem_body_text=problem_body_text+down_url+"\n"
    problem_body_text=problem_body_text+language_list[1]
    create_file=create_dir+"\\"+problem_file_name+language_list[2]
    with open(create_file,"w",encoding="utf-8") as problem_python:
        problem_python.write(problem_body_text)

def step_download(tr_list,i,language_list,html_image=True,korea_name=False):
    dir_name=tr_list[i].td.get_text()
    dir_name=dir_name+"_"+tr_list[i].td.find_next_sibling("td").get_text()
    dir_name=folder_path+"\\"+dir_name
    # print(dir_name)
    createFolder(dir_name) # 디렉토리 생성
    problem_url=baekjoon_url+tr_list[i].td.find_next_sibling("td").a["href"]
    # print(problem_url)
    response=requests.get(problem_url)
    response.raise_for_status()
    soup=bs4.BeautifulSoup(response.text,"lxml")
    problem_tr_list=soup.find("tbody").find_all("tr")
    # print(problem_tr_list) # 리스트가 문제 수 의 2배로 되어 있음. 문제사이 텍스트가 추가되어 있음.
    for j in range(0,len(problem_tr_list),2):
        problem_num=problem_tr_list[j].find("td").get_text()
        problem_title=problem_tr_list[j].find("td").find_next_sibling("td").find_next_sibling("td").get_text()
        problem_title=not_avaible_str_in_file(problem_title)
        
        if korea_name: 
            problem_file_name=problem_num+". "+problem_title # 파이썬 파일 이름 (한글 O)
        else: 
            problem_file_name="{}".format(i+1)+"_"+problem_num # 파일 이름 (한글 X)

        create_dir=dir_name+"\\"+problem_num+"_"+problem_title
        createFolder(create_dir)
        # print(create_file)
        down_url=baekjoon_url+problem_tr_list[j].find("a")["href"]
        response=requests.get(down_url)
        response.raise_for_status()
        soup=bs4.BeautifulSoup(response.text,"lxml")

        if html_image: html_image_down(soup,create_dir,problem_file_name)

        problem_language_down(soup,down_url,create_dir,problem_file_name,language_list)
    


url="https://www.acmicpc.net/step"
response=requests.get(url)
response.raise_for_status()
soup=bs4.BeautifulSoup(response.text,"lxml")

tr_list=soup.find("tbody").find_all("tr")

C_language_list=["/*","*/",".c"]
Python_language_list=["'''","'''",".py"] # html_image korea_name=True로 한번 다운해야 함.

for i in range(len(tr_list)):
    if i==12 or i==49: # 문제 수정 중
        continue
    step_download(tr_list,i,language_list=["/*","*/",".c"],html_image=True,korea_name=False)
