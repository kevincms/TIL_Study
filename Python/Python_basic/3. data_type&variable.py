# 파이썬은 변수를 선언할 떄 따로 자료형을 정의하지 않는다.
count=1

test_int=1 # 1. 정수
print(str(count)+".",test_int,type(test_int))
count+=1

test_float=1.1 # 2. 실수
print(str(count)+".",test_float,type(test_float))
count+=1

test_str="Hello World" # 3. 문자열
print(str(count)+".",test_str,type(test_str)) 
count+=1

test_bool=1<2 # 4, 참과 거짓
print(str(count)+".",test_bool,type(test_bool))
count+=1

test_list=[1,1.1,"Hello World"] # 5. list 안에는 무엇이든 넣을 수 있음. list 안에 list를 넣는 것도 가능함.
print(str(count)+".",test_list,type(test_list)) 
count+=1

# 줄바꿈의 영향을 받지 않는 문자열
link_break_str="""
Hello
World
"""
print(str(count)+".",link_break_str,type(link_break_str))
count+=1

# data type별로의 연산
print(str(count)+".",1+1*2,type(1+1*2))
count+=1
print(str(count)+".","1"+"1",type("1"+"1"))
count+=1
