# 파이썬은 변수를 선언할 떄 따로 자료형을 정의하지 않는다.
count=1

test_int=1 # 1. 정수
print("%d."%count,test_int,type(test_int))
count+=1

test_float=1.1 # 2. 실수
print("%d."%count,test_float,type(test_float))
count+=1

test_str="Hello World" # 3. 문자열
print("%d."%count,test_str,type(test_str)) 
count+=1

test_bool=1<2 # 4, 참과 거짓
print("%d."%count,test_bool,type(test_bool))
count+=1

test_list=[1,1.1,"Hello World"] # 5. list 안에는 무엇이든 넣을 수 있음. list 안에 list를 넣는 것도 가능함
print("%d."%count,test_list,type(test_list)) 
count+=1

test_dict={0:"영",1:"일",2:"이"} # key 값은 int, float, str, bool 모두 가능함 (list는 안됨)
print("%d."%count,test_dict,type(test_dict)) # 6. dictionary는 key와 value로 이루어져 있음
count+=1

test_tuple=(0,1)
print("%d."%count,test_tuple,type(test_tuple)) # 7. tuple은 수정할 수 없음 (대신 계산속도가 빠름)
count+=1

test_set={1,2,3,4,5,4,2,3,}
print("%d."%count,test_set,type(test_set)) # 8. set(집합)은 중복이 안되고, 순서가 없음
count+=1

# type을 다른 type으로 변경 가능
test_type=test_list
print("%d"%count,test_type,type(test_type)) # 9.
count+=1

test_type=tuple(test_type)
print("%d"%count,test_type,type(test_type)) # 10.
count+=1

test_type=set(test_type)
print("%d"%count,test_type,type(test_type)) # 11.
count+=1

# 줄바꿈의 영향을 받지 않는 문자열
link_break_str="""
Hello
World
"""
print("%d."%count,link_break_str,type(link_break_str))
count+=1

# data type별로의 연산
print("%d."%count,1+1*2,type(1+1*2))
count+=1
print("%d."%count,"1"+"1",type("1"+"1"))
count+=1