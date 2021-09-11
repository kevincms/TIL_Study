count=1
print(str(count)+".",1,type(1))
count+=1
print(str(count)+".",1.1,type(1.1))
count+=1
print(str(count)+".","Hello World",type("Hello World"))
count+=1
print(str(count)+".",[1,1.1,"Hello World"],type([1,1.1,"Hello World"])) # list 안에는 무엇이든 넣을 수 있음. list 안에 list를 넣는 것도 가능함.
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
