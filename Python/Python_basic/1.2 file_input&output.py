import os
foler_path=os.path.dirname(__file__)
file_name="\\test_file.txt"
create_file=foler_path+file_name
language=["Python","C","Java","C++","Go","JavaScript","Swift","C#"]
count=1

print("%d. %s"%(count,create_file)) # 1. 파일경로+파일이름

test_file=open(create_file,"w",encoding="utf8")
print("[%d. %s]"%(count,language[count-1]),file=test_file) # w :  덮어쓰기
count+=1
test_file.close()

test_file=open(create_file,"a",encoding="utf8")
test_file.write("[%d. %s]"%(count,language[count-1])) # a : 이어쓰기
count+=1
test_file.close()

count=2
test_file=open(create_file,"r",encoding="utf8")
print("%d.\n%s"%(count,test_file.read())) # 모두 읽어오기
count+=1
test_file.close()

test_file=open(create_file,"r",encoding="utf8")
print("%d. %s"%(count,test_file.readline()),end="") # 한줄씩 읽어오기
count+=1
test_file.close()

# with은 자원을 획득 후 바로 반납할 때 사용한다. (with EXPRESSION [as VARIAVLE])
with open(create_file,"r",encoding="utf8") as test_file: # with을 사용하면 close를 하지 않아도 됨
    print("%d. %s"%(count,test_file.readlines())) # 리스트로 모두 읽어오기

