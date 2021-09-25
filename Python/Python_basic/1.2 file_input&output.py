language=["Python","C","Java","C++","Go","JavaScript","Swift","C#"]
count=1

test_file=open("test_file.txt","w",encoding="utf8")
print("%d. %s"%(count,language[count-1]),file=test_file) # w :  덮어쓰기 
count+=1

test_file.close()

test_file=open("test_file.txt","a",encoding="utf8")
test_file.write("%d. %s"%(count,language[count-1])) # a : 이어쓰기
count+=1

test_file.close()

test_file=open("test_file.txt","r",encoding="utf8")
print(test_file.read()) # 모두 읽어오기
test_file.close()

test_file=open("test_file.txt","r",encoding="utf8")
print(test_file.readline(),end="") # 한줄씩 읽어오기
test_file.close()

with open("test_file.txt","r",encoding="utf8") as test_file: # with을 사용하면 close를 하지 않아도 됨.
    print(test_file.readlines()) # 리스트로 모두 읽어오기

