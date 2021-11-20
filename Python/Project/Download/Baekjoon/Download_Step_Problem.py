import os
import requests
import bs4

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
            
            
            
    
folder_path="D:\\Baekjoon_step_problem"
url="https://www.acmicpc.net/step"
baekjoon_url="https://www.acmicpc.net/"

response=requests.get(url)
response.raise_for_status()
soup=bs4.BeautifulSoup(response.text,"lxml")

tr_list=soup.find("tbody").find_all("tr")

for i in range(len(tr_list)):
    if i==12 or i==49: # 문제 수정 중
        continue
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
        problem_file_name=problem_num+". "+problem_title
        create_dir=dir_name+"\\"+problem_num+"_"+problem_title
        createFolder(create_dir)
        create_file=create_dir+"\\"+problem_file_name+".html"
        # print(create_file)
        down_url=baekjoon_url+problem_tr_list[j].find("a")["href"]
        response=requests.get(down_url)
        response.raise_for_status()
        # with open(create_file,"w",encoding="utf-8") as down_html:
        #     down_html.write(response.text)
        soup=bs4.BeautifulSoup(response.text,"lxml")
        problem_body_list=soup.find("div",attrs={"id":"problem-body"}).find_all("div",attrs={"class":"col-md-12"})
        problem_body_text="\'\'\'\n"
        if problem_body_list[1].find("h2").get_text()=="제한": # 예외처리
            problem_body_text=problem_body_text+problem_body_list[0].find("h2").get_text()+"\n -"
            problem_body_text=problem_body_text+problem_body_list[0].find("div",attrs={"class":"problem-text"}).get_text().strip()+"\n"
            problem_body_text=problem_body_text+down_url+"\n"
            problem_body_text=problem_body_text+"\'\'\'"
            create_file=create_dir+"\\"+problem_file_name+".py"
            with open(create_file,"w",encoding="utf-8") as problem_python:
                problem_python.write(problem_body_text)
            continue
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
        problem_body_text=problem_body_text+"\'\'\'"
        create_file=create_dir+"\\"+problem_file_name+".py"
        with open(create_file,"w",encoding="utf-8") as problem_python:
            problem_python.write(problem_body_text)