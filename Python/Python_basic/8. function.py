count=1
language=["Python","C","Java","C++","Go","JavaScript","Swift","C#"]

def test_func(test_num,test_language):
    print("%d. %s"%(test_num,test_language))

test_func(count,language[count-1]) # 1. 함수의 파라미터 순서대로 입력
count+=1

test_func(test_language=language[count-1],test_num=count) # 2. 함수의 파라미터를 지정해서 입력
count+=1

def variable_args_func(test_num,*test_language): # (args=arguments 약자)
    print("{}. {}".format(test_num,test_language))

variable_args_func(count,"Python","C","Java","C++") # 3. 위치가변인자 (tuple의 형태로 전달됨)
count+=1

def variable_kwargs_func(test_num,**test_language): # (kwargs=keyword arguments 약자)
    print("{}. {}".format(test_num,test_language))

variable_kwargs_func(count,one="Python",two="Java") # 4. 키워드가변인자 (dictionary의 형태로 전달됨)
count+=1

def local_variable_func():
    count=100
    print("%d. 지역변수"%count) # 100. 지역변수 (전역변수 count에 영향이 없음)

def global_variable_func():
    global count
    print("%d.   전역변수"%count) # 5. 전역변수 사용 시 global

local_variable_func()
global_variable_func()

def return_func(count):
    return count+1

count=return_func(count)
print("%d. return"%count) # 6. return 을 이용해 지역변수의 값을 꺼내올 수 있음
count+=1