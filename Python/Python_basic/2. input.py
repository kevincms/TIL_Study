# input() = 입력 받은 문자열

# 1. Python
count=1
# language=input("What is your language?\n") # 입력을 받을 떄 안내문을 넣을 수 있음
# print("%d. Hello %s "%(count,language))
count+=1

# 2. 20201415 조민석
# num, name=input().split() # str_function split() 을 이용해 분리하여 입력받을 수 있음 (기본 반환 list)
# print("%d. 학번 : %s 이름 : %s "%(count,num,name)) # input()은 숫자로 넣어도 문자열로 반환
count+=1

# 3. 3.14 1.59 2.65
# a, b, c=map(float,input().split()) # map을 이용해 문자열을 특정 형으로 한꺼번에 바꿀 수 있음
# print("%d. %.2f %.2f %.2f"%(count, a, b, c))
count+=1