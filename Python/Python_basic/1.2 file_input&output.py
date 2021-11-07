import os

foler_path=os.path.dirname(__file__)
file_name="\\test_file.txt"
create_file=foler_path+file_name
language=["Python","C","Java","C++","Go","JavaScript","Swift","C#"]
count=1

print("%d. %s"%(count,create_file)) # 1. 파일경로+파일이름

test_file=open(create_file,mode="w",encoding="utf8") # w : 덮어쓰기, 생성
print("[%d. %s]"%(count,language[count-1]),file=test_file) 
count+=1
test_file.close()

test_file=open(create_file,"a",encoding="utf8") # a : 이어쓰기
test_file.write("[%d. %s]"%(count,language[count-1])) 
count+=1
test_file.close()

count=2
test_file=open(create_file,"r",encoding="utf8") # r : 모두 읽어오기
print("%d.\n%s"%(count,test_file.read())) # 2.
count+=1
test_file.close()

test_file=open(create_file,"r",encoding="utf8") 
print("%d. %s"%(count,test_file.readline()),end="") # 3. 한줄씩 읽어오기
count+=1
test_file.close()

# with은 자원을 획득 후 바로 반납할 때 사용한다. (with EXPRESSION [as VARIAVLE])
with open(create_file,"r",encoding="utf8") as test_file: # with을 사용하면 close를 하지 않아도 됨
    print("%d. %s"%(count,test_file.readlines())) # 4. 리스트로 모두 읽어오기

'''
'r' : 읽기용 (기본값)
'w' : 쓰기용
'x' : 독점적인 파일 만들기용 (이미 존재하는 경우에는 실패)
'a' : 이어쓰기영

't' 텍스트 모드 (기본값)
'b' 바이너리 모드
'+' 갱신(읽기 및 쓰기)용으로 엽니다
ex) 'r''rt''w+''w+b''r+''r+b'
'''
