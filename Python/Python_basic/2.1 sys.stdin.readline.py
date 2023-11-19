import sys

# 1. Python
count=1
# language=sys.stdin.readline() # input과 달리 안내문을 넣을 수 없음
# print("%d. Hello %s "%(count,language)) # 뒤의 개행문자(줄바꿈)을 포함해 입력받음 (한줄씩 입력)
count+=1

# 2. 20201415 조민석
# input=sys.stdin.readline # input에 비해 길기 떄문에 변수에 대입해 사용할 수 있음
# num, name=input().split()
# print("%d. 학번 : %s 이름 : %s "%(count,num,name))
count+=1

# 3. 문자열
# string=input()
# print("%d. %s %s"%(count, string.rstrip(), string)) # str_function rstrip()을 이용해 개행문자를 제거할 수 있음
count+=1

# 4. list
list=list(map(str,input().split()))
print("{}. {}".format(count,list)) # str_function rstrip()을 이용해 개행문자를 제거할 수 있음
count+=1